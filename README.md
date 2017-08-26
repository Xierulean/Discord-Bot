# Discord-Bot

[![Python Version](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-351/)

A simple bot created for Discord. The bot can perform basic functions such as play music in voice channels, silly text commands, create and store information into databases.

If you would like to invite the bot to your server, click the link below!

https://discordapp.com/oauth2/authorize?client_id=343639761900273666&scope=bot

# Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Commands](#commands)
  * [Database](#database)
  * [Help](#help)
  * [Miscellaneous](#miscellaneous)
  * [Music](#music)
  * [Owner Only](#owner-only)
  * [Time](#time)
  * [No Category](#no-category)
- [FAQ](#faq)
- [Support](#support)
- [Contribution](#contribution)
  * [Code Style](#code-style)


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

# Command Categories

The following are the commands that the bot can perform in their respective categories.

## Database

| Command		| Command Description 								| Example										| Command Aliases							|
|:--------------|:--------------------------------------------------|:----------------------------------------------|:--------------------------------------	|
| >>alldb		| Give list of all databases saved. 				| >>alldb										| >>db, >>DB, >>allDB, >>showdb, >>showDB	|
| >>newEntry	| Add a database entry or create new database.		| >>newEntry database_name category information | >>newdb, >>newDB, >>entry, >>insert		|

## Help

| Command		| Command Description 								| Example										| Command Aliases						|
|:--------------|:--------------------------------------------------|:----------------------------------------------|:--------------------------------------|
| >>pyhelp		| Search in the Python website.						| /pyhelp Strings								| >>py_help, >>phy, >>python_help		| 

## Miscellaneous

| Command		| Command Description 								| Example										| Command Aliases						|
|:--------------|:--------------------------------------------------|:----------------------------------------------|:--------------------------------------|
| >>ask			| Ask the bot a yes/no/maybe question.				| >>ask Is this bot awesome?					| >>8ball								|
| >>hug			| Give someone or yourself a hug!					| >>hug @User_name								| None									|
| >>pick			| Pick between given choices. The choices are separated by " or "								| >>pick red or blue or green			| None									|

## Music

| Command		| Command Description 								| Example										| Command Aliases						|
|:--------------|:--------------------------------------------------|:----------------------------------------------|:--------------------------------------|
| >>join		| Joins a voice channel.							| >>join										| None									|
| >>pause		| Pauses the currently played song.					| >>pause										| None									|
| >>play		| Plays a song.										| >>play youtube_link_here						| None									|
| >>playing		| Shows info about the currently played song.		| >>playing										| None									|
| >>resume		| Resumes the currently played song.				| >>resume										| None									|
| >>skip		| Vote to skip a song.								| >>skip										| None									|
| >>stop		| Stops playing audio and leaves the voice channel.	| >>stop										| None									|
| >>summon		| Summons the bot to join your voice channel.		| >>summon										| None									|
| >>volume		| Sets the volume of the currently playing song.	| >>volume 60									| None									|

## Owner Only

| Command		| Command Description 								| Example										| Command Aliases						|
|:--------------|:--------------------------------------------------|:----------------------------------------------|:--------------------------------------|
| >>restart		| Restarts the bot. Only the bot owner can use this command. Note: At the moment the restart command will only work for Windows.	| >>restart				| None									|
| >>shutdown	| Logs the bot off Discord and shuts it down. Only the bot owner can use this command.												| >>shutdown			| >>disconnect							|

## Time

| Command		| Command Description 								| Example										| Command Aliases						|
|:--------------|:--------------------------------------------------|:----------------------------------------------|:--------------------------------------|
| >>date 		| Returns the current date and time					| >>date										| None									|
| >>join_date	| Gives the user's server join date					| >>join_date									| None									|

## No Category

| Command		| Command Description 								| Example										| Command Aliases						|
|:--------------|:--------------------------------------------------|:----------------------------------------------|:--------------------------------------|
| >>help		| Shows all of the commands that the bot can do.	| >>help										| None									|

# FAQ

1. My bot was running fine a few days ago but lately, it suddenly stopped working and gave some errors about missing modules or cogs.
- If the bot reports an error related to "cogs" or "missing modules", try to reinstall the bot by following the [installation instructions](#installation) or only reinstall the parts that is giving the error. Reinstalling may fix the problem because dependencies may occasionally become out of date or some files may have gotten corrupted.

# Support

If there are any questions or issues with installation, please open an issue here: https://github.com/DMCTruong/Discord-Bot/issues
It is recommended that the following information is included before submitting an issue so that the issue may be resolved quicker.

1. The goal that is trying to be achieved. What was the expected outcome?
2. What actually happened? If there was an error message, what was the error message?
3. What is the version of the CLI you are using?
4. If the problem is related to implementing a feature, please also include the code in question.

# Contribution

If you would like to help out with the bot, feel free to fork the project, add your changes, then create a pull request.
Plus, I'm also looking for a new bot logo!

## Code Style

The indentation standard for this project is 4 spaces.