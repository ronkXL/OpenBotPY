import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '--')

@client.event
async def on_ready():
    print('OpenBot#6578 is ready to use')

client.run('your token here:D')