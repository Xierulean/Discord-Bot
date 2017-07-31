##########################################################################################
# Program Name:     Discord Bot
# Author:           DMCTruong
# Last Updated:     July 31, 2017
# Description:      A general purpose bot written for Discord
##########################################################################################

import discord
from discord.ext import commands
import asyncio
import configurations
import pyrebase

bot = commands.Bot(configurations.PREFIX)
firebase = pyrebase.initialize_app(configurations.FIREBASE_INFO)
db = firebase.database()

class Database:
	def __init__(self, bot):
		self.bot = bot

	# Command: Shows names of minecraft location stored in database
	# Usage: /show_location_names
	@bot.command()
	async def show_location_names(self):
		all_locations = db.child("minecraft").child("locations").shallow().get()
		response = "I know about:\n{}".format("\n".join(all_locations.val()))
		return await self.bot.say(response)

	# Command: Adds minecraft location then store it into database
	# Usage: /add_location name x y z
	@bot.command()
	async def add_location(self, name, x, y, z):
		x, y, z = map(int, [x, y, x])
		db.child("minecraft").child("locations").update(
			{name: "{} {} {}".format(x, y, z)}
		)
		return await self.bot.say("I've added {} to the database.".format(name))

	# Command: Shows minecraft location in the database
	# Usage: /show_locations name
	@bot.command()
	async def show_locations(self, name):
		location = db.child("minecraft").child("locations").child(name).get()
		x, y, z = location.val().split()
		response = "{} is at X {}, Y {}, Z {}".format(name, x, y, z)
		return await self.bot.say(response)

	# Command: Allows user to create a new database or add new entry
	# Usage: /newEntry Pokemon Electric Pikachu
	@bot.command()
	async def newEntry(self, dbname, name, entry):
		db.child("Discord").child(dbname).update({name: "{}".format(entry)})
		updateSuccess = "The database, {}, has been updated sucessfully with entry, {}: {}.".format(dbname, name, entry)
		return await self.bot.say(updateSuccess)

	# Command: Returns all of the database names stored in Pyrebase
	# Usage: /alldb
	@bot.command()
	async def alldb(self):	
		getAlldb = db.child("Discord").shallow().get()
		allDatabases = "The databases that are available are:\n - {}".format("\n - ".join(getAlldb.val()))
		return await self.bot.say(allDatabases)	