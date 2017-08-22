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
import datetime
import subprocess
import time
from time import localtime, strftime

bot = commands.Bot(configurations.PREFIX)

class Time:
    def __init__(self, bot):
        self.bot = bot
	
    @bot.command(pass_context=True)
    async def date(self):
        """Returns the current date and time"""

        date_time = strftime("The date is %A, %B %d, %Y at %I:%M %p in %Z.", localtime())
        print(date_time)
        await self.bot.say(date_time)

    #async def alarm(self, ctx, *, mins: int, member: discord.Member=None):