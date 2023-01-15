import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

async def on_message(message):
  if message.author == client.user:
    return

    
  if message.content.startswith('$train'):
    await message.channel.send('@everyone Training!!! First SHR And HR+ will be Host And Co Host')

client.run(os.getenv('TOKEN'))