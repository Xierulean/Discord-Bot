##########################################################################################
# Program Name:     Discord Bot
# Author:           DMCTruong
# Last Updated:     July 27, 2017
# Description:      A general purpose bot written for Discord
##########################################################################################


# To do List:
#	- Add a tutorial on how to install and get the keys for the configurations
#	- Add a way for the user to create new databases
#	- Add better documentation of the code
#	- Add bot help command
#	- Create a database for Vindictus's scroll price estimates (with permmissions)
#	- Reorganize the code or separate the code into different files
#	- Update the README.md
#	- Return the user's avatar?

# Known Issues:
#	- The bot seems to buffer a lot when playing music. 
#		Hopefully, the issue and a solution will be found soon.



# Note to self: Download and install ffmeg
# Also, check this out: https://pypi.python.org/pypi/googletrans

import discord
from discord.ext import commands
from urllib.parse import urlencode
import logging
import asyncio
import configurations
import pyrebase
import random
import time

# Note to self: \ = new line for python

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = '*{0.title}* uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing ' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()

# Commands: For voice chat
class Music:
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        """Joins a voice channel."""
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            await self.bot.say('Already in a voice channel...')
        except discord.InvalidArgument:
            await self.bot.say('This is not a voice channel...')
        else:
            await self.bot.say('Ready to play audio in ' + channel.name)

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        """Summons the bot to join your voice channel."""
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            await self.bot.say('You are not in a voice channel.')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        """Plays a song.

        If there is a song currently in the queue, then it is
        queued until the next song is done playing.

        This command automatically searches as well from YouTube.
        The list of supported sites can be found here:
        https://rg3.github.io/youtube-dl/supportedsites.html
        """
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            await self.bot.say('Enqueued ' + str(entry))
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def volume(self, ctx, value : int):
        """Sets the volume of the currently playing song."""

        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            await self.bot.say('Set the volume to {:.0%}'.format(player.volume))

    @commands.command(pass_context=True, no_pm=True)
    async def pause(self, ctx):
        """Pauses the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.pause()

    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        """Resumes the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(pass_context=True, no_pm=True)
    async def stop(self, ctx):
        """Stops playing audio and leaves the voice channel.

        This also clears the queue.
        """
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        """Vote to skip a song. The song requester can automatically skip.

        3 skip votes are needed for the song to be skipped.
        """

        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            await self.bot.say('Not playing any music right now...')
            return

        voter = ctx.message.author
        if voter == state.current.requester:
            await self.bot.say('Requester requested skipping song...')
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            if total_votes >= 3:
                await self.bot.say('Skip vote passed, skipping song...')
                state.skip()
            else:
                await self.bot.say('Skip vote added, currently at [{}/3]'.format(total_votes))
        else:
            await self.bot.say('You have already voted to skip this song.')

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):
        """Shows info about the currently played song."""

        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            await self.bot.say('Not playing anything.')
        else:
            skip_count = len(state.skip_votes)
            await self.bot.say('Now playing {} [skips: {}/3]'.format(state.current, skip_count))
			
bot = commands.Bot(configurations.PREFIX) 
bot.add_cog(Music(bot))
firebase = pyrebase.initialize_app(configurations.FIREBASE_INFO)
db = firebase.database()

# Also, don't forget to run "pip install pyrebase"

print("Please wait while the Bot logs in ...")

eightBallResponses = [
    "Sure, go for it!",
    "Sure but I'm not entirely certain",
    "Perhaps?",
    "No, that's a terrible idea!",
    ]

funnyPrefix = [
    "Pink Unicorn ",
    "Papa Smurf ",
    "King ",
    "Queen ",
    "Prince ",
    "Princess, "
    ]
killResponses = [
    " threw %s thrown off the boat!",
    " gave %s a headbutt!",
    " unleashed a Kraken on %s!",
    " gave %s a bearhug!"
    ]


# Upon login, say ...
@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("========================")
    
# Command: Say :joy: and echo what user said
@bot.command(pass_context=True)
async def echo(ctx, *, echo: str):
    await bot.delete_message(ctx.message)
    await bot.say("*headbutt* " + echo)
    
# Command: Playfully interact with a member
@bot.command(pass_context=True)
async def kill(ctx, *, member: discord.Member=None):
    if member is None:
        await bot.say(ctx.message.author.mention + ": I cannot kill someone unless you tell me who you want to kill!")
        return
		
    if member.id == configurations.BOT_ID:
        await bot.say(ctx.message.author.mention + ": You can't kill me!")
    elif member.id == configurations.BOT_OWNER_ID and member.id == ctx.message.author.id:
        await bot.say(ctx.message.author.mention + ": A-Are you sure you want me to kill you mom?")
    elif member.id == configurations.BOT_OWNER_ID:
        await bot.say("You can't kill my master!")
    elif member.id == ctx.message.author:
        await bot.say(ctx.message.author.mention + ": Why do you want me to kill you?")
    else: 
        random.seed(time.time())
        choiceResponse = killResponses[random.randrange(len(killResponses))] % member.mention
        await bot.say(ctx.message.author.mention + " " + choiceResponse)
 
# Command: Hug someone or yourself
@bot.command(pass_context=True)
async def hug(ctx, *, member: discord.Member=None):
    if member is None:
        await bot.say(ctx.message.author.mention + " gave a hug.")
    else:
        if member.id == ctx.message.author.id:
            await bot.say("A bear gave " + member.mention + " a bear hug.")
        else:
            await bot.say(member.mention + " has been hugged by " + ctx.message.author.mention + ".")    
	  
# Command: Make the bot pick a choice in the form of: choice1,choice2
@bot.command(pass_context=True)
async def pick(ctx, *, choices: str):
    choicesArr = choices.split(" or ")
    chosen = choicesArr[random.randrange(len(choicesArr))]
    await bot.say(ctx.message.author.mention + ": I choose " + chosen)
  
# Command: Add a funny prefix to everyone's nickname in the server as a joke
@bot.command(pass_context=True)
async def trollEveryone(ctx):
    for member in ctx.message.server.members:
        try:
            random.seed(time.time())
            addPrefix = funnyPrefix[random.randrange(len(funnyPrefix))]		
            await bot.change_nickname(member, addPrefix + member.name)
        except discord.errors.Forbidden:
            pass
    await bot.say(ctx.message.author.mention + ": Everyone's nickname is changed!! Buahahaha")
	
# Command: Return everyone's nickname in the server back to normal after using /trollEveryone command
@bot.command(pass_context=True)
async def noMoreTroll(ctx):
    for member in ctx.message.server.members:
        try:
            await bot.change_nickname(member, member.name)
        except discord.errors.Forbidden:
            pass
    await bot.say(ctx.message.author.mention + ": Everyone's nickname is now changed back to normal!")
 
 
# Command: Lets the user to search through Python's documentation
@bot.command(aliases=["py_help", "pyh", "python_help"])
async def pyhelp(*args):
    print(args)
    url = ("https://docs.python.org/3/search.html?{}"
           "&check_keywords=yes&area=default".format(
           urlencode({'q': ' '.join(args)})
           ))
    return await bot.say(url)

	
# Command: "8ball"
@bot.command(pass_context=True)
async def ask(ctx):
    random.seed(time.time())
    askResponse = eightBallResponses[random.randrange(len(eightBallResponses))]
    await bot.say(ctx.message.author.mention + " " + askResponse)

# Command: Bot Help, returns all available commands
async def help(ctx):
    await bot.say()
	
# Command: Shows names of minecraft location stored in database
# Usage: !show_location_names
@bot.command()
async def show_location_names():
    all_locations = db.child("minecraft").child("locations").shallow().get()
    response = "I know about:\n{}".format("\n".join(all_locations.val()))
    return await bot.say(response)

# Command: Adds minecraft location then store it into database
# Usage: !add_location name x y z
@bot.command()
async def add_location(name, x, y, z):
    x, y, z = map(int, [x, y, x])
    db.child("minecraft").child("locations").update(
        {name: "{} {} {}".format(x, y, z)}
    )
    return await bot.say("I've added {} to the database.".format(name))

# Command: Shows minecraft location in the database
# Usage: !show_locations name
@bot.command()
async def show_locations(name):
    location = db.child("minecraft").child("locations").child(name).get()
    x, y, z = location.val().split()
    response = "{} is at X {}, Y {}, Z {}".format(name, x, y, z)
    return await bot.say(response)

	
	
# Note to self: How to push data into database example

# If python doesn't run for windows git bash and path is already added then type: alias python='winpty python.exe'
# python
# import configurations
# import pyrebase
# firebase = pyrebase.initialize_app(configurations.FIREBASE_INFO)
# db = firebase.database()
# db.child("minecraft").child("locations").update({"spawn": "0 0 0"})
# db.child("minecraft").child("locations").update({"end portal": "35 134 50"})



bot.run(configurations.BOT_TOKEN)