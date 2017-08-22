##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 21, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################


# To do List:
#	- Add a calculator
#	- Add a log function
#		Command log turned off by default
#		Error log turned on by default
#	- Add a translator: https://pypi.python.org/pypi/googletrans
#	- Add a better tutorial on how to install and get the keys for the configurations
#	- Add better documentation of the code
#	- Return the user's avatar?
#	- Update pyrebase commands



# Known Issues:
#	1. The bot seems to buffer a lot when playing music. 
#		Hopefully, the issue and a solution will be found soon.
#	- Solution: If the bot seems to be buffering, try changing the server location

import discord
from discord.ext import commands
import asyncio
import configurations

from modules import database
from modules import help
from modules import miscellaneous
from modules import music
from modules import owner_only
from modules import timer
			
bot = commands.Bot(configurations.PREFIX) 

bot.add_cog(database.Database(bot))
bot.add_cog(help.Help(bot))
bot.add_cog(miscellaneous.Miscellaneous(bot))
bot.add_cog(music.Music(bot))
bot.add_cog(owner_only.Owner_Only(bot))
bot.add_cog(timer.Time(bot))

print("\nPlease wait while the Bot logs in ...")

# Upon login, say ...
@bot.event
async def on_ready():
    print("\nLogged in as:\n")
    print("Username : " + bot.user.name)
    print("ID Number: " + bot.user.id)
    print('\nType "::help" in the Discord chat for the list of commands.')
    print("=============================================")
	
    await bot.change_presence(game=discord.Game(name='::help for commands!'))

@bot.command(pass_context=True)
async def join_date(ctx, member: discord.Member = None):
    """Gives user's server join date"""

    if member is None:
       member = ctx.message.author
       await bot.say('{0} joined the server on {0.joined_at}'.format(member))
	
bot.run(configurations.BOT_TOKEN)