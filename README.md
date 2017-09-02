# Discord-Bot

![Development Period](https://img.shields.io/badge/Development-Alpha-orange.svg)
[![Python Version](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-351/)

A simple bot created for Discord. The bot can perform basic functions such as play music in voice channels, silly text commands, create and store things into databases.

Mew is a demonstration bot, to try out the bot's commands, feel free to click the link below and invite Mew to your server! 

https://discordapp.com/oauth2/authorize?client_id=353420001451180032&scope=bot

Note: When inviting the bot to your server, the amount of uptime that the bot have is dependent on its hosting service so there will be moments when it is offline, but the bot will be kept online as much as possible.

# Table of Contents

- [Discord-Bot](#discord-bot)
- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
- [Installation](#installation)
  * [Installing Python and Pip](#installing-python-and-pip)
  * [Installing Virtualenv](#installing-virtualenv)
  * [Adding Path Variable for Virtualenv](#adding-path-variable-for-virtualenv)
  * [Running Virtualenv](#running-virtualenv)
  * [Installing the Requirements](#installing-the-requirements)
  * [Setting up the Configurations](#setting-up-the-configurations)
  * [Running the Bot](#running-the-bot)
- [Command Categories](#command-categories)
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

1. Python 3.5
2. Discord.py
3. pyrebase
4. youtube-dl

# Installation

**Important:** Throughout the installation instructions, if typing ``python3`` or ``pip3`` does not work, try typing ``python`` or ``pip`` instead.

## Installing Python and Pip

If you have Python and Pip already installed, you may skip to [Step 3](#installing-virtualenv).

1.	To begin, check to see if you have Python installed. To do this, type the command
		<pre>python3 --version</pre>
	If you get an answer similar to this, ``Python 3.4.3``, it means you already have Python installed.  
     If not, you will need to install Python. Head over to Python's [download page](https://www.python.org/downloads/) and follow the installation instructions for your system.

2.	Next, type ``pip3 --version`` to check if Pip is installed.  
	You should receive an answer similar to this if Pip is installed.
		<pre>pip 1.5.4 from /usr/lib/python3/dist-packages (python 3.4)</pre>
	If not, then visit [this page](https://packaging.python.org/tutorials/installing-packages/#install-pip-setuptools-and-wheel) to install Pip.

## Installing Virtualenv

For Step 3 and 4, If you already know how to setup a virtual environment, please skip to [Step 6](#installing-the-requirements).

**Note:** Because newer Versions are not backwards compatible, setting up a virtual environment is reccommended to avoid having the newer installations overwrite the existing ones.
   
3.	To install a virtual environment, type:
    	<pre>pip3 install --user virtualenv</pre>
    For Unix systems, if the command above does not work, try this command:
    	<pre>sudo pip3 install virtualenv </pre>
    Once the installation is complete, check to see if installation was successful:
		<pre>virtualenv --version</pre>
    If you receive Virtualenv's version number after typing the command, then skip to [Step 5](#running-virtualenv).
    If not, proceed to [Step 4](#adding-path-variable-for-virtualenv).
   
## Adding Path Variable for Virtualenv

4.	Open ``.bash_profile`` with an Text Editor of your choosing. Add Virtualenv's Path Variable to the file, save, and then source the file.

**Adding Path Variable Example**:  
Vim Text Editor will be used throughout this example, but any Text Editor will do.  
First, open the ``.bash_profile`` by typing, ``vim ~/.bash_profile``.  
Press ``i`` to go into Insert mode and then copy the following line into the file.
	<pre>alias virtualenv3='~/Library/Python/VERSION_NUMBER/bin/virtualenv'</pre>
Where it says ``VERSION_NUMBER``, replace it with the first two numbers of your Python Version.
____
>For example, let's say that your Python Version is ``Python 3.4.3``.  
From ``Python 3.4.3`` replace ``VERSION_NUMBER`` with ``3.4`` which results:
	<pre>alias virtualenv3='~/Library/Python/3.4/bin/virtualenv'</pre>
Press ``ESC``, ``:``, ``x``, and then ``ENTER`` to save and exit the editor.  
____
Finally, type ``source ~/.bash_profile`` to finish up Step 4.  
Check to see if Virtualenv is installed properly with ``virtualenv --version``.
        
## Running Virtualenv

5.	Once you have virtualenv installed, it's time to make a virtual environment and run it. 

Replace ``VIRTUALENV_FOLDER`` with the name of the folder where you want to create your virtual environment in.
	<pre>cd VIRTUALENV_FOLDER/</pre>

Replace ``VIRTUALENV_NAME`` with the name that you pick for your virtual environment.
	<pre>virtualenv VIRTUALENV_NAME</pre>

Do the same for this next command.
    <pre>source VIRTUALENV_NAME/bin/activate</pre>

____
>Example:
    <pre>
    cd My_Virtualenv_Folder/
    virtualenv My_Virtualenv
    source My_Virtualenv/bin/activate
    </pre>
____
        
## Installing the Requirements

Once everything is setup, it is time to install the Bot's requirements.

6.	Installing **Python 3.5.1**: ``pip3 install python3.5``  
	For Unix systems: ``sudo apt-get install python3.5``  
7. Installing **Discord.py**: ``python3.5 -m pip install -U discord.py[voice]``  
	For Unix systems: ``pip3 install -U discord.py[voice]``
8. Installing **Pyrebase**: ``pip3 install pyrebase``
9. Installing **youtube-dl**: ``pip3 install --upgrade youtube_dl``
10. Download the bot files: ``clone https://github.com/DMCTruong/Discord-Bot.git``  

If you don't have git installed.  
	**Windows**:  
    	https://git-scm.com/download/win  
    **Ubuntu**:
<pre>
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
</pre>


## Setting up the Configurations

Finally, you are almost there! The configuration file just needs a few information.
11. Begin by opening configurations.py preferably with Notepad++, Vim or a similar program.
12. Follow the instructions in the configuration file.
       
## Running the Bot

13. Once all of the information in the configurations file is filled out, the bot is ready to run, just double click Bot.py! For more information on what commands the bot can use, type ``>>help`` in the Discord chat.

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

2. I had invited the bot to my server and it was working fine before but one day, it suddenly disappeared from the server.
- For the server owner, head to ``Server Settings``. Under ``User Management``, click ``Members``. Look for the bot, kick it from the server then reinvite it. If the bot still does not show up, the user can try adding a role to the bot as for some servers, the offline list is invisible. If else, the user can try and relog to fix it.

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