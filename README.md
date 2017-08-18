# Discord-Bot

[![Python Version](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-351/)

A simple bot created for Discord. The bot can perform basic functions such as play music in voice channels, silly text commands, create and store information into databases.

If you would like to invite the bot to your server, click the link below!

https://discordapp.com/oauth2/authorize?client_id=343639761900273666&scope=bot

# Requirements

1. Python
2. Discord.py
3. pyrebase
4. youtube-dl

# Installation

1. Download and install the latest version of Python. Be sure to add Python's path to the Enviromental Variables!

Note: For this next section, if typing python3 does not work, try typing just python.

2. Next, to install Discord.py, open a command line and type: python3 -m pip install -U discord.py[voice]
3. Then, install pyrebase by typing the following in a command line: python3 pip install pyrebase
4. Finally, download and install youtube-dl: python3 pip install --upgrade youtube_dl
5. After that, open /docs/configurations.py (preferably with Notepad++ or a similar program)and the tutorials in the file will help you retrieve the information that the bot requires to run.
6. Once all of the information in the configurations file is filled out, the bot is ready to run, double click Bot.py! For more information on what commands the bot can use, type /help in the Discord chat.

# Commands

| Category		| Command		| Command Description 											| Example										| Command Aliases						|
|:--------------|:--------------|:--------------------------------------------------			|:----------------------------------------------|:--------------------------------------|
| Database		| /newEntry		| Add a database entry or create new database.					| /newEntry database_name category information 	| /newdb, /newDB, /entry, /insert		|
| Database		| /alldb		| Give list of all databases saved. 							| /alldb										| /db, /DB, /allDB, /showdb, /showDB	|
| Help			| /pyhelp		| Search in the Python website.									| /pyhelp Strings								| /py_help, /phy, /python_help			| 
| Miscellaneous	| /ask			| Ask the bot a yes/no/maybe question.							| /ask Is this bot awesome?						| /8ball								|
| Miscellaneous	| /pick			| Pick between given choices									| /pick red or blue								| None									|
| Miscellaneous	| /kill			| Playfully interact with a member.								| /kill @User_name								| None									|
| Miscellaneous	| /hug			| Give someone or yourself a hug!								| /hug @User_name								| None									|
| Miscellaneous	| /trollEveryone	| Add a funny prefix to everyone's nickname as joke			| /trollEveryone								| None									|
| Miscellaneous	| /noMoreTroll	| Removes funny prefix from everyone's nickname	from /trollEveryone command.	| /noMoreTroll		| None									|
| Music			| /pause			| Pauses the currently played song.							| /pause										| None									|
| Music			| /volume		| Sets the volume of the currently playing song.				| /volume 60									| None									|
| Music			| /play			| Plays a song.													| /play youtube_link_here						| None									|
| Music			| /join			| Joins a voice channel.										| /join											| None									|
| Music			| /resume		| Resumes the currently played song.							| /resume										| None									|
| Music			| /skip			| Vote to skip a song.											| /skip											| None									|
| Music			| /summon		| Summons the bot to join your voice channel.					| /summon										| None									|
| Music			| /stop			| Stops playing audio and leaves the voice channel.				| /stop											| None									|
| Music			| /playing		| Shows info about the currently played song.					| /playing										| None									|
| Time			| /uptime 		| Timer for how long bot runs until need restart.				| /uptime										| None									|
| No Category	| /join_date	| Gives the user's server join date								| /join_date									| None									|
| No Category	| /restart		| Restarts the bot. Only the bot owner can use this command.	| /restart										| None									|
| No Category	| /shutdown		| Logs the bot off Discord and shuts it down. Only the bot owner can use this command.		| /shutdown			| /disconnect							|
| No Category	| /help			| Shows all of the commands that the bot can do.				| /help											| None									|

# FAQ

1. My bot was running fine a few days ago but lately, it suddenly stopped working and gave some errors about missing modules or cogs.
- If the bot reports an error related to "cogs" or "missing modules", try to reinstall the bot by following the [installation instructions](#installation) or only reinstall the parts that is giving the error. Reinstalling may fix the problem because dependencies may occasionally become out of date or some files may have gotten corrupted.

# Contribution

If you would like to help out with the bot. Feel free to fork the project, add your changes, then create a pull request.