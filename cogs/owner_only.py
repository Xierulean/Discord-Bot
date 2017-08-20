##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 20, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################

import discord
from discord.ext import commands
import asyncio
import configurations
import os
import subprocess
import sys

bot = commands.Bot(configurations.PREFIX)

class Owner_Only:
    def __init__(self, bot):
        self.bot = bot
	
    @bot.command(pass_context=True, aliases=["disconnect"])
    async def shutdown(self, ctx):
        """Logs the bot off Discord and shuts it down"""

        if ctx.message.author.id == configurations.BOT_OWNER_ID:
            await self.bot.say("Shutting down, see you next time!")
            await self.bot.close()
        else:
            await self.bot.say("Sorry, only the bot owner can use this command.")

    @bot.command(pass_context=True)
    async def restart(self, ctx):
        """Restarts the bot."""

        if ctx.message.author.id == configurations.BOT_OWNER_ID:
            await self.bot.say("I am restarting, I'll be back in a second!")	
            subprocess.Popen("restart.sh", shell=True)
            print("Bot is shutting down ...")
            await self.bot.close()
        else:
            await self.bot.say("Sorry, only the bot owner can use this command.")