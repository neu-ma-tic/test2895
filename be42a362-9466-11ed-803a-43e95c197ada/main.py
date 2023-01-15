

from keep_alive import keep_alive

import discord
import os

Greetings = "Your Holy Slave Has Been Awaken To Serve You Master Blast. Your Desire Is My Life's Command."

client = discord.Client()

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
    if message.content.startswith("!Greetings"):
        await client.send_message(message.channel, Greetings)

@client.event
async def on_message(message):
    if message.content.startswith("!What is your favourite server?"):
        await client.send_message(message.channel, "The Great Blast Gaming Of Course!")








keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)