import datetime

import discord
from discord.ext import commands

import os
from replit import db

client = commands.Bot(command_prefix='-', help_command=None)

# server and message to be edited
guildChannelID = int(os.environ['guildChannelID'])
embedMsgID = int(os.environ['embedMsgID'])

def updateEmbedFields():
  embed = discord.Embed(
    title = 'Team Status',
    description = 'Use **-status text** to update your status \n **-st** for the busy ones)',
    footer = 'Last Update'
  )
  embed.timestamp = datetime.datetime.utcnow()
  userIDs = db.keys();
  for id in userIDs:
    embed.add_field(name=client.get_user(id), value=db[id])
    print(client.get_user(id))
  return embed

async def updateMessage():
  channel = client.get_channel(guildChannelID)
  partMsg = channel.get_partial_message(embedMsgID)
  embedObj = updateEmbedFields()
  await partMsg.edit(embed = embedObj)

# starting the bot 
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
  updateMessage()

# user command handling
@client.command(name='status', aliases=['stat', 'st'])
async def status_command(ctx, status=""):
  db[ctx.message.author.id] = status
  updateMessage()

# bot login
client.run(os.environ['token'])



# workflow
# on ready: 
#   update embed from db
# on command:
#   get user
#   check db for user
#   create new/ update existing

# db structure
# user-id : status
# note - user name is extracted from id
