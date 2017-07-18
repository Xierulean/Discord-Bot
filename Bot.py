import discord
from discord.ext import commands
import logging
import asyncio

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
	print("Logged in as:")
	print(bot.user.name)
	print(bot.user.id)
	print("========================")

@bot.command()
async def test():
	await bot.say("Testing? Testing...")

bot.run("Insert bot token here.")