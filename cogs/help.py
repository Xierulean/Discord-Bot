##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 7, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
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

	# Usage Example: /py_help Strings
	@bot.command(aliases=["py_help", "pyh", "python_help"])
	async def pyhelp(self, *args):
		"""Search in the Python website."""
		print(args)
		url = ("https://docs.python.org/3/search.html?{}"
			"&check_keywords=yes&area=default".format(
			urlencode({'q': ' '.join(args)})
			))
		return await self.bot.say(url)