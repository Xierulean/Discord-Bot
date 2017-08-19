##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 19, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################


# To do List:
#	- Add a calculator
#	- Add a log function
#		Command log turned off by default
#		Error log turned on by default
#	- Add a translator: https://pypi.python.org/pypi/googletrans
#	- Add a tutorial on how to install and get the keys for the configurations
#	- Add better documentation of the code
#	- Move /restart, /shutdown, and /join_date to a cog
#	- Return the user's avatar?



# Known Issues:
#	1. The bot seems to buffer a lot when playing music. 
#		Hopefully, the issue and a solution will be found soon.
#	- Solution: If the bot seems to be buffering, try changing the server location
#
#	2. When /restart command is used the first time, the first window that was used to run the bot does not close.
#		But if the /restart command is used multiple times, the windows that were used to run the previous
#		bot instances closes properly.

import discord
from discord.ext import commands
import asyncio
import configurations
import logging
import os
import subprocess
import sys

from cogs import database
from cogs import help
from cogs import miscellaneous
from cogs import music
from cogs import timer
			
bot = commands.Bot(configurations.PREFIX) 

bot.add_cog(database.Database(bot))
bot.add_cog(miscellaneous.Miscellaneous(bot))
bot.add_cog(help.Help(bot))
bot.add_cog(music.Music(bot))
bot.add_cog(timer.Time(bot))

# run_timer = timer.Time();

print("\nPlease wait while the Bot logs in ...")

# Upon login, say ...
@bot.event
async def on_ready():
	print("\nLogged in as:\n")
	print("Username : " + bot.user.name)
	print("ID Number: " + bot.user.id)
	print("\nType /help in the Discord chat for the list of commands.")
	print("=============================================")
	
	await bot.change_presence(game=discord.Game(name='/help for commands!'))
	#run_timer.uptime()
	

@bot.command(pass_context=True, aliases=["disconnect"])
async def shutdown(ctx):
	"""Logs the bot off Discord and shuts it down"""
	if ctx.message.author.id == configurations.BOT_OWNER_ID:
		await bot.say("Shutting down, see you next time!")
		await bot.close()
	else:
		await bot.say("Sorry, only the bot owner can use this command.")

@bot.command(pass_context=True)
async def restart(ctx):
	"""Restarts the bot."""
	if ctx.message.author.id == configurations.BOT_OWNER_ID:
		await bot.say("I am restarting, I'll be back in a second!")	
		subprocess.Popen("restart.sh", shell=True)
		print("Bot is shutting down ...")
		await bot.close()
	else:
		await bot.say("Sorry, only the bot owner can use this command.")

@bot.command(pass_context=True)
async def join_date(ctx, member: discord.Member = None):
	"""Gives user's server join date"""
	if member is None:
		member = ctx.message.author
		await bot.say('{0} joined the server on {0.joined_at}'.format(member))
	
	
bot.run(configurations.BOT_TOKEN)