import discord
from discord.ext import commands
import logging
import asyncio
import random
import time

bot = commands.Bot(command_prefix="/")
killResponses = [" threw %s thrown off the boat!", " gave %s a headbutt!", " unleashed a Kraken on %s!", " gave %s a bearhug!"]

# Note to self: \ = new line for python
print("Please wait while the Bot logs in ...")


@bot.event
async def on_ready():
	print("Logged in as:")
	print(bot.user.name)
	print(bot.user.id)
	print("========================")

# Say "Testing? Testing..."
@bot.command()
async def test():
	await bot.say("Testing? Testing...")

# Say :joy: then echo what user said
@bot.command(pass_context = True)
async def echo2(ctx, *, echo: str):
	await bot.delete_message(ctx.message)
	await bot.say(":joy:" + echo)

# Playfully kill a member
@bot.command(pass_context = True)
async def kill(ctx, *, member : discord.Member =  None):
	if member is None:
		await bot.say(ctx.message.author.mention + ": I cannot kill someone unless you tell me who you want to kill!")
		return
		
	if member.id == "319302490518454272":
		await bot.say(ctx.message.author.mention + ": You can't kill me!")
	elif member.id == "164202667118297090" and member.id == ctx.message.author.id:
		await bot.say(ctx.message.author.mention + ": A-Are you sure you want me to kill you mom?")
	elif member.id == "164202667118297090":
		await bot.say("You can't kill my master!")
	elif member.id == ctx.message.author:
		await bot.say(ctx.message.author.mention + ": Why do you want me to kill you?")
	else: 
		random.seed(time.time())
		choice = killResponses[random.randrange(len(killResponses))] % member.mention
		await bot.say(ctx.message.author.mention + " " + choice)
                
@bot.command(pass_context = True)
async def hug(ctx, *, member : discord.Member = None):
        if member is None:
                await bot.say(ctx.message.author.mention + " gave a hug.")
        else:
            if member.id == ctx.message.author.id:
                await bot.say("A bear gave " + member.mention + " a bear hug.")
            else:
                await bot.say(member.mention + " has been hugged by " + ctx.message.author.mention + ".")
	
bot.run("Insert bot token here.")

