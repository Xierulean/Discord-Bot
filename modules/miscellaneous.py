##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 21, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################

import discord
from discord.ext import commands
import asyncio
import configurations
import random
from random import randint
import time

bot = commands.Bot(configurations.PREFIX)

eightBallResponses = [
    "Sure, go for it!",
    "Sure but I'm not entirely certain",
    "Perhaps?",
    "No, that's a terrible idea!",
    ]

class Miscellaneous:
    def __init__(self, bot):
        self.bot = bot
	
    @bot.command(pass_context=True, aliases=["8ball"])
    async def ask(self, ctx):
        """Ask the bot a yes/no/maybe question."""

        random.seed(time.time())
        askResponse = eightBallResponses[random.randrange(len(eightBallResponses))]
        print(ctx.message.author.mention + " " + askResponse)
        await self.bot.say(ctx.message.author.mention + " " + askResponse)
		
    @bot.command(pass_context=True)
    async def hug(self, ctx, *, member: discord.Member=None):
        """Give someone or yourself a hug!"""

        generate_hug = randint(1, 16)
        gif_url = "https://dmctruong.000webhostapp.com/.Discord/gifs-hugs/hug" + str(generate_hug) + ".gif"
        if member is None:
            print("*hugs* " + gif_url)
            await self.bot.say("*hugs*\n" + gif_url)
        else:
            if member.id == ctx.message.author.id:
                print("*hugs* " + gif_url)
                await self.bot.say("*hugs*\n" + gif_url)
            else:
                print(ctx.message.author.mention + " gave " + member.mention + " a hug! " + gif_url)
                await self.bot.say(ctx.message.author.mention + " gave " + member.mention + " a hug!\n" + gif_url)

    @bot.command(pass_context=True)
    async def pick(self, ctx, *, choices: str):
        """Pick between given choices"""

        choicesArr = choices.split(" or ")
        chosen = choicesArr[random.randrange(len(choicesArr))]
        print(ctx.message.author.mention + ": I choose " + chosen)
        await self.bot.say(ctx.message.author.mention + ": I choose " + chosen)