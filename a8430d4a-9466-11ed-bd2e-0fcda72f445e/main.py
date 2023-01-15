import discord
from discord.ext import commands
from discord import FFmpegPCMAudio


token = "ODgxNTcxMzE1NzM4Mzc4MzEx.YSuxRA.3IlzamWYwIu5F9V-OslR4BrRgjk"
client = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print("bot is online")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("astronaut.mp3")
        player = voice.play(source)
    else:
        await ctx.send("join a vc dumbass")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("disconnected")
    else:
        await ctx.send("im not in a vc")

    

client.run(token);