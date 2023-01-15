import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

intents = discord.Intents().all()
intents.members = True
intents.messages = True

@client.command()
async def load(ctx, extension):
    client.load_extention(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extention(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
      client.load_extention(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))