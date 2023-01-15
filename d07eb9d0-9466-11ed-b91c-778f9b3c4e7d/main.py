import discord
import os 
import requests
import json

client = discord.Client()

def get_funfact():
  response = requests.get('https://api.fungenerators.com/random')
  json_data = json.loads(response.text)
@client.event
async def on_ready():
  print('we are online ({0.user})'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('hello')
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!funfact'):
      await message.channel.send('')
client.run('OTM3MDQyMTkyNzMwNTY2NzA2.YfV-jA.8t8LEBsKEbi5H1y8ygBN1mGiUss')

#^this turns the bot online

