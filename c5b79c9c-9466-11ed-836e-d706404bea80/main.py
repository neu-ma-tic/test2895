import os
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from replit import db
default_prefix = '*'






try:
    prefix = db["prefix"]
except KeyError:
    prefix = '*'
    db["prefix"] = prefix



client = commands.Bot(
    command_prefix = prefix,
    help_command = None
)


@client.event
async def on_ready():
    print('ready')






@client.command(
    name= 'ping',
    alias= []
)
async def ping(ctx: Context):
    await ctx.channel.send(f':ping_pong: Pong für {ctx.author.mention}:ping_pong:')















TOKEN = os.environ['TOKEN']
client.run(TOKEN)
