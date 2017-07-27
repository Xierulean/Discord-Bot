##########################################################################################
# Program Name:		Discord Bot
# Author:			DMCTruong
# Last Updated:		July 25, 2017
# Description:		A bot that was created for Discord chat with various functions
##########################################################################################


# To do List:
#	- Add a tutorial on how to install and get the keys for the configurations
#	- Add better documentation of the code
#	- Add bot help command
#	- Create a database for Vindictus's scroll price estimates (with permmissions)
#	- Reorganize the code or separate the code into different files
#	- Update the README.md

# Note to self: Download and install ffmeg
# Also, check this out: https://pypi.python.org/pypi/googletrans


import discord
from discord.ext import commands
from urllib.parse import urlencode
import logging
import asyncio
import configurations
import pyrebase
import random
import time

# Note to self: \ = new line for python

bot = commands.Bot(configurations.PREFIX)
firebase = pyrebase.initialize_app(configurations.FIREBASE_INFO)
db = firebase.database()

# Also, don't forget to run "pip install pyfirebase"

print("Please wait while the Bot logs in ...")

eightBallResponses = [
    "Sure, go for it!",
    "Sure but I'm not entirely certain",
    "Perhaps?",
    "No, that's a terrible idea!",
    ]

funnyPrefix = [
    "Pink Unicorn ",
    "Papa Smurf ",
    "King ",
    "Queen ",
    "Prince ",
    "Princess, "
    ]
killResponses = [
    " threw %s thrown off the boat!",
    " gave %s a headbutt!",
    " unleashed a Kraken on %s!",
    " gave %s a bearhug!"
    ]


# Upon login, say ...
@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("========================")
    
# Command: Say :joy: and echo what user said
@bot.command(pass_context=True)
async def echo(ctx, *, echo: str):
    await bot.delete_message(ctx.message)
    await bot.say(":joy:" + echo)
    
# Command: Playfully interact with a member
@bot.command(pass_context=True)
async def kill(ctx, *, member: discord.Member=None):
    if member is None:
        await bot.say(ctx.message.author.mention + ": I cannot kill someone unless you tell me who you want to kill!")
        return
		
    if member.id == configurations.BOT_ID:
        await bot.say(ctx.message.author.mention + ": You can't kill me!")
    elif member.id == configurations.BOT_OWNER_ID and member.id == ctx.message.author.id:
        await bot.say(ctx.message.author.mention + ": A-Are you sure you want me to kill you mom?")
    elif member.id == configurations.BOT_OWNER_ID:
        await bot.say("You can't kill my master!")
    elif member.id == ctx.message.author:
        await bot.say(ctx.message.author.mention + ": Why do you want me to kill you?")
    else: 
        random.seed(time.time())
        choiceResponse = killResponses[random.randrange(len(killResponses))] % member.mention
        await bot.say(ctx.message.author.mention + " " + choiceResponse)
 
# Command: Hug someone or yourself
@bot.command(pass_context=True)
async def hug(ctx, *, member: discord.Member=None):
    if member is None:
        await bot.say(ctx.message.author.mention + " gave a hug.")
    else:
        if member.id == ctx.message.author.id:
            await bot.say("A bear gave " + member.mention + " a bear hug.")
        else:
            await bot.say(member.mention + " has been hugged by " + ctx.message.author.mention + ".")    
	  
# Command: Make the bot pick a choice in the form of: choice1,choice2
@bot.command(pass_context=True)
async def pick(ctx, *, choices: str):
    choicesArr = choices.split(" or ")
    chosen = choicesArr[random.randrange(len(choicesArr))]
    await bot.say(ctx.message.author.mention + ": I choose " + chosen)
  
# Command: Add a funny prefix to everyone's nickname in the server as a joke
@bot.command(pass_context=True)
async def trollEveryone(ctx):
    for member in ctx.message.server.members:
        try:
            random.seed(time.time())
            addPrefix = funnyPrefix[random.randrange(len(funnyPrefix))]		
            await bot.change_nickname(member, addPrefix + member.name)
        except discord.errors.Forbidden:
            pass
    await bot.say(ctx.message.author.mention + ": Everyone's nickname is changed!! Buahahaha")
	
# Command: Return everyone's nickname in the server back to normal after using /trollEveryone command
@bot.command(pass_context=True)
async def noMoreTroll(ctx):
    for member in ctx.message.server.members:
        try:
            await bot.change_nickname(member, member.name)
        except discord.errors.Forbidden:
            pass
    await bot.say(ctx.message.author.mention + ": Everyone's nickname is now changed back to normal!")
 
 
# Command: Lets the user to search through Python's documentation
@bot.command(aliases=["py_help", "pyh", "python_help"])
async def pyhelp(*args):
    print(args)
    url = ("https://docs.python.org/3/search.html?{}"
           "&check_keywords=yes&area=default".format(
           urlencode({'q': ' '.join(args)})
           ))
    return await bot.say(url)

	
# Command: "8ball"
@bot.command(pass_context=True)
async def ask(ctx):
    random.seed(time.time())
    askResponse = eightBallResponses[random.randrange(len(eightBallResponses))]
    await bot.say(ctx.message.author.mention + " " + askResponse)

# Command: Bot Help, returns all available commands
async def help(ctx):
    await bot.say()
	
# Command: Shows names of minecraft location stored in database
# Usage: !show_location_names
@bot.command()
async def show_location_names():
    all_locations = db.child("minecraft").child("locations").shallow().get()
    response = "I know about:\n{}".format("\n".join(all_locations.val()))
    return await bot.say(response)

# Command: Adds minecraft location then store it into database
# Usage: !add_location name x y z
@bot.command()
async def add_location(name, x, y, z):
    x, y, z = map(int, [x, y, x])
    db.child("minecraft").child("locations").update(
        {name: "{} {} {}".format(x, y, z)}
    )
    return await bot.say("I've added {} to the database.".format(name))

# Command: Shows minecraft location in the database
# Usage: !show_locations name
@bot.command()
async def show_locations(name):
    location = db.child("minecraft").child("locations").child(name).get()
    x, y, z = location.val().split()
    response = "{} is at X {}, Y {}, Z {}".format(name, x, y, z)
    return await bot.say(response)

# Note to self: How to push data into database example
# If python doesn't run for windows git bash and path is already added then type: alias python='winpty python.exe'
# python
# import configurations
# import pyrebase
# firebase = pyrebase.initialize_app(configurations.FIREBASE_INFO)
# db = firebase.database()
# db.child("minecraft").child("locations").update({"spawn": "0 0 0"})
# db.child("minecraft").child("locations").update({"end portal": "35 134 50"})

bot.run(configurations.BOT_TOKEN)