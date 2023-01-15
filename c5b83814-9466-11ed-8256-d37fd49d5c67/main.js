import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("ODM0MzU5NTI0MDA5MDUwMTYz.YH_v3A.2MWaTFyVXpV59SQzGIOtWf39ctk")