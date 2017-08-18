##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 18, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################

import discord
from discord.ext import commands
import asyncio
import configurations
import time

# Todo:
#	Add a function that lets the bot returns the time and date
#	This cog will also used for reminders
#	Repurpose the timer for a different function.

bot = commands.Bot(configurations.PREFIX)

class Time:
	def __init__(self, bot):
		self.bot = bot
	
	@bot.command(pass_context=True)
	async def uptime(self, ctx, *, member: discord.Member=None):
		"""Timer for how long bot runs until need restart."""
		now = time.time()
		stop = now + 17100
		print("The uptime timer is now starting. It is set to alarm 4 hours and 45 minutes from now.")
		while True:
			if time.time() > stop:
				await self.bot.send_message(ctx.message.author, "The end is near, please be ready to restart me in 15 minutes.")
				return print("The end is near, please be ready to restart me 15 minutes.")
				