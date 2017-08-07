##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 7, 2017
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

bot = commands.Bot(configurations.PREFIX)

class Time:
	# The bot is currently being hosted on Cloud9. Every 5 hours, the service will stop the bot.
	# This method is to help keep track of when it is close to the time that the bot shuts down
	# so that the bot can restart without much delay.
	
	def __init__(self, bot):
		self.bot = bot
	
	@bot.command(pass_context=True)
	async def uptime(self, ctx, *, member: discord.Member=None):
		"""Timer for how long bot runs until need restart."""
		now = time.time()
		stop = now + 17100
		while True:
			if time.time() > stop:
				await self.bot.send_message(ctx.message.author, "The end is nigh, please be ready to restart me in 15 minutes.")
				return print("The end is nigh, please be ready to restart me 15 minutes.")
				