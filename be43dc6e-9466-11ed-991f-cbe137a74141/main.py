import os

import discord


DISCORD_TOKEN = os.getenv('TOKEN')




client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

async def on_member_join(member):
    print('HI')
client.run(os.getenv('TOKEN'))
