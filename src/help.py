##########################################################################################
# Program Name:     Discord Bot
# Author:           DMCTruong
# Last Updated:     July 31, 2017
# Description:      A general purpose bot written for Discord
##########################################################################################

import discord
from discord.ext import commands
from urllib.parse import urlencode
import asyncio
import configurations

bot = commands.Bot(configurations.PREFIX)

class Help:
	def __init__(self, bot):
		self.bot = bot	

	# Command: Lets the user to search through Python's documentation
	# Usage: /py_help Strings
	@bot.command(aliases=["py_help", "pyh", "python_help"])
	async def pyhelp(self, *args):
		print(args)
		url = ("https://docs.python.org/3/search.html?{}"
			"&check_keywords=yes&area=default".format(
			urlencode({'q': ' '.join(args)})
			))
		return await self.bot.say(url)
	
	# Command: Bot Help, returns all available commands
	# Usage: /help
	async def help(self, ctx):
		await self.bot.say()