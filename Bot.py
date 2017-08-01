##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 1, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################


# To do List:
#	- Add a tutorial on how to install and get the keys for the configurations
#	- Add better documentation of the code
#	- Add a calculator
#	- Update the README.md
#	- Return the user's avatar?

# Known Issues:
#	- The bot seems to buffer a lot when playing music. 
#		Hopefully, the issue and a solution will be found soon.

# Also, check this out: https://pypi.python.org/pypi/googletrans

import discord
from discord.ext import commands
import asyncio
import configurations
import logging

from cogs import database
from cogs import help
from cogs import miscellaneous
from cogs import music
			
bot = commands.Bot(configurations.PREFIX) 

bot.add_cog(database.Database(bot))
bot.add_cog(miscellaneous.Miscellaneous(bot))
bot.add_cog(help.Help(bot))
bot.add_cog(music.Music(bot))

print("Please wait while the Bot logs in ...")

# Upon login, say ...
@bot.event
async def on_ready():
	print("\nLogged in as:\n")
	print("Username : " + bot.user.name)
	print("ID Number: " + bot.user.id)
	print("\nType /help in the Discord chat for the list of commands.")
	print("=============================================")
bot.run(configurations.BOT_TOKEN)