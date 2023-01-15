import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('AlexBot is Online!')

client.run("NzE0MjE2NzY5MTU3NTk1MjUw.XtlHdw.4SPtzUiPGdnlJbk3_SCd7273sv0") 
@client.command
async def plzhelp(ctx):
    await ctx.send('no help for u lmao')
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    client.run("NzE0MjE2NzY5MTU3NTk1MjUw.XtlHdw.4SPtzUiPGdnlJbk3_SCd7273sv0") 
@client.command()
async def hey(ctx):
 await client.say("Hello There!")
 client.run("NzE0MjE2NzY5MTU3NTk1MjUw.XtlHdw.4SPtzUiPGdnlJbk3_SCd7273sv0")  


