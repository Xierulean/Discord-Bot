##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 8, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################


# To do List:
#	- Add a calculator
#	- Add a translator: https://pypi.python.org/pypi/googletrans
#	- Add a tutorial on how to install and get the keys for the configurations
#	- Add better documentation of the code
#	- Update the /hug command
#	- Update the README.md
#	- Return the user's avatar?

# Known Issues:
#	- The bot seems to buffer a lot when playing music. 
#		Hopefully, the issue and a solution will be found soon.

import discord
from discord.ext import commands
import asyncio
import configurations
import logging
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

print("Please wait while the Bot logs in ...")

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
async def shutdown():
	"""Logs the bot off Discord and shuts it down"""
	await bot.say("Shutting down, see you next time!")
	await bot.close()
		
	
bot.run(configurations.BOT_TOKEN)