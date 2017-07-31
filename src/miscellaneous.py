##########################################################################################
# Program Name:     Discord Bot
# Author:           DMCTruong
# Last Updated:     July 31, 2017
# Description:      A general purpose bot written for Discord
##########################################################################################

import discord
from discord.ext import commands
import asyncio
import configurations
import random
import time

bot = commands.Bot(configurations.PREFIX)

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


class Miscellaneous:
	def __init__(self, bot):
		self.bot = bot
	
	# Command: Make the bot pick a choice in the form of: choice1,choice2
	@bot.command(pass_context=True)
	async def pick(self, ctx, *, choices: str):
		choicesArr = choices.split(" or ")
		chosen = choicesArr[random.randrange(len(choicesArr))]
		await self.bot.say(ctx.message.author.mention + ": I choose " + chosen)
		
	# Command: Playfully interact with a member
	@bot.command(pass_context=True)
	async def kill(self, ctx, *, member: discord.Member=None):
		if member is None:
			await self.bot.say(ctx.message.author.mention + ": I cannot kill someone unless you tell me who you want to kill!")
			return
		
		if member.id == configurations.BOT_ID:
			await self.bot.say(ctx.message.author.mention + ": You can't kill me!")
		elif member.id == configurations.BOT_OWNER_ID and member.id == ctx.message.author.id:
			await self.bot.say(ctx.message.author.mention + ": A-Are you sure you want me to kill you mom?")
		elif member.id == configurations.BOT_OWNER_ID:
			await self.bot.say("You can't kill my master!")
		elif member.id == ctx.message.author:
			await self.bot.say(ctx.message.author.mention + ": Why do you want me to kill you?")
		else: 
			random.seed(time.time())
			choiceResponse = killResponses[random.randrange(len(killResponses))] % member.mention
			await self.bot.say(ctx.message.author.mention + " " + choiceResponse)
 
	# Command: Hug someone or yourself
	@bot.command(pass_context=True)
	async def hug(self, ctx, *, member: discord.Member=None):
		if member is None:
			await self.bot.say(ctx.message.author.mention + " gave a hug.")
		else:
			if member.id == ctx.message.author.id:
				await self.bot.say("A bear gave " + member.mention + " a bear hug.")
			else:
				await self.bot.say(member.mention + " has been hugged by " + ctx.message.author.mention + ".")    
			
	# Command: Add a funny prefix to everyone's nickname in the server as a joke
	@bot.command(pass_context=True)
	async def trollEveryone(self, ctx):
		for member in ctx.message.server.members:
			try:
				random.seed(time.time())
				addPrefix = funnyPrefix[random.randrange(len(funnyPrefix))]		
				await self.bot.change_nickname(member, addPrefix + member.name)
			except discord.errors.Forbidden:
				pass
		await self.bot.say(ctx.message.author.mention + ": Everyone's nickname is changed!! Buahahaha")
	
	# Command: Return everyone's nickname in the server back to normal after using /trollEveryone command
	@bot.command(pass_context=True)
	async def noMoreTroll(self, ctx):
		for member in ctx.message.server.members:
			try:
				await self.bot.change_nickname(member, member.name)
			except discord.errors.Forbidden:
				pass
		await self.bot.say(ctx.message.author.mention + ": Everyone's nickname is now changed back to normal!")

	# Command: "8ball"
	@bot.command(pass_context=True)
	async def ask(self, ctx):
		random.seed(time.time())
		askResponse = eightBallResponses[random.randrange(len(eightBallResponses))]
		await self.bot.say(ctx.message.author.mention + " " + askResponse)