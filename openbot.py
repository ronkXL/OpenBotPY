import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '--')

@client.event
async def on_ready():
    print('OpenBot#6578 is ready to use')

@client.event
async def on_member_join(member):
    print (f'{member} has joined the squad')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the squad')

@client.command()
async def latency(ctx):
    await ctx.send(f'Latency is {round(client.latency * 1000)}')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['add your responses here']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
client.run('')