##########################################################################################
# Program Name :     Discord Bot
# Author       :     DMCTruong
# Last Updated :     August 31, 2017
# License      :     MIT
# Description  :     A general purpose bot written for Discord               
##########################################################################################


# <-------------------------- Discord Bot Configurations --------------------------------->

# The following are information that the bot requires before the bot can run.
# Once all of the following information is filled out, the bot will be ready to use. Just 
# double click on Bot.py and you will be able to use all of the bot commands in discord! 

# For more information about what commands the bot can use, type >>help in 
# the Discord chat.

# <--------------------------- Important Configurations ---------------------------------->

PREFIX = ">>"

# Currently, the default command prefix is ">>"
# For example: >>echo Hello World
# You are welcome to change the command prefix to anything you wish.

BOT_OWNER_ID = "Bot Owner's ID here"
BOT_ID = "Bot's ID here"

# Please follow this tutorial to get various Discord IDs.
# https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-

BOT_TOKEN = "Bot's Token here"

# This tutorial will show how to get a Discord Bot token.
# https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

FIREBASE_INFO = {
    "apiKey": "Firebase API Key here",
    "authDomain": "Firebase Auth Domain here",
    "databaseURL": "Firebase Database Url here",
    "projectId": "Firebase Project ID here",
    "storageBucket": "Firebase Storage Bucket here",
    "messagingSenderId": "Firebase Messaging Sender ID here"
}

# To get Firebase info, please follow the tutorial below. You do not need to follow the entire tutorial, 
# it is only until you get all of the information needed to fill out the required data above.
# https://firebase.google.com/docs/web/setup

# <=======================================================================================>
# If you are reading this, congratulations, you've just finished configurating the Bot 
# and you are now ready to go! Just double click Bot.py and then type >>help in the 
# Discord chat for the list of commands that the Bot can do! 

# Beyond this point are additional features that you can configure but the Bot will 
# still work if you leave these settings as default.

# Other than that, thank you for using DMCTruong's Discord Bot!

# For support, please submit a "New Issue" to the link below and I will do my best to help.
# https://github.com/DMCTruong/Discord-Bot/issues

# <=======================================================================================>

# <----------------------------- Logging Configurations ---------------------------------->

# The following are logging settings. For now, these features are set to off by default
# because the amount of information that gets output can be a lot.
# If you would like to turn these features on, change the "NO" to "YES."

COMMAND_LOG = "NO"
ERROR_LOG = "NO"
DISCORD_LOG = "NO"

# <--------------------------------------------------------------------------------------->