##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 31, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################

import discord
from discord.ext import commands
import asyncio
import configurations
import pyrebase

bot = commands.Bot(configurations.PREFIX)
firebase = pyrebase.initialize_app(configurations.FIREBASE_INFO)
db = firebase.database()
storage = firebase.storage()

class Database:
    def __init__(self, bot):
        self.bot = bot
		
    @bot.command(aliases=["db, DB, allDB, , showdb, showDB"])
    async def alldb(self):
        """Give list of all databases saved"""

        getAlldb = db.child("Discord").shallow().get()
        allDatabases = "The databases that are available are:\n - {}".format("\n - ".join(getAlldb.val()))		
        print(allDatabases)
        return await self.bot.say(allDatabases)	

    @bot.command(aliases=["newdb, newDB, entry, insert"])
    async def newEntry(self, dbname, name, entry):
        """Add a database entry or create new database"""

        db.child("Discord").child(dbname).update({name: "{}".format(entry)})
        updateSuccess = "The database, {}, has been updated sucessfully with entry, {}: {}.".format(dbname, name, entry)
        print(updatesuccess)
        return await self.bot.say(updateSuccess)