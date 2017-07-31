##########################################################################################
# Program Name:     Discord Bot
# Author:           DMCTruong
# Last Updated:     July 31, 2017
# Description:      A general purpose bot written for Discord
##########################################################################################


# To do List:
#	- Add a tutorial on how to install and get the keys for the configurations
#	- Add better documentation of the code
#	- Add bot help command
#	- Add a calculator
#	- Create a database for Vindictus's scroll price estimates (with permmissions)
#	- Reorganize the code or separate the code into different files
#	- Update the README.md
#	- Return the user's avatar?

# Known Issues:
#	- The bot seems to buffer a lot when playing music. 
#		Hopefully, the issue and a solution will be found soon.


# Note to self: Download and install ffmeg
# Also, check this out: https://pypi.python.org/pypi/googletrans
# Also, don't forget to run "pip install pyrebase"

import discord
from discord.ext import commands
import asyncio
import configurations
import database
import help
import logging
import miscellaneous
import music
			
bot = commands.Bot(configurations.PREFIX) 

bot.add_cog(database.Database(bot))
bot.add_cog(miscellaneous.Miscellaneous(bot))
bot.add_cog(help.Help(bot))
bot.add_cog(music.Music(bot))

print("Please wait while the Bot logs in ...")

# Upon login, say ...
@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("========================")

	
# Command: A test command: The bot echos back what the user said
# Usage: /echo Hello there
@bot.command(pass_context=True)
async def echo(ctx, *, echo: str):
    await bot.delete_message(ctx.message)
    await bot.say("Echo: " + echo)
	  
bot.run(configurations.BOT_TOKEN)