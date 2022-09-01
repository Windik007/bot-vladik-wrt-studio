import discord
from discord.ext import commands 


client = discord.Client()

client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix=".")
bot.remove_command('help')


bot.run("Nzg5ODAwNzMzMzI3MjI4OTM5.GF8M8H.qy9v3zBWEG-rNPynUANnip05sPj3mjhCUDqFOA")