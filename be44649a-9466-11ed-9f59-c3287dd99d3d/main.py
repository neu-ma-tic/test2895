import os
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='!')


# I can only make the server owner works
def is_guild_owner(ctx):
    return ctx.guild.owner_id == ctx.author.id


# def is_bot_owner(ctx):
#     return client.owner_id == ctx.author.id


# Tell us when the client is ready
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Karuta"))
    print("Logged in as {0.user}\n".format(client))


# Load the selected file from cogs
@client.command()
@commands.check(is_guild_owner)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Hi, bot owner\n\'{extension}\' is loaded")
    

# Unload the selected file from cogs
@client.command()
@commands.check(is_guild_owner)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Hi, bot owner\n\'{extension}\' is unloaded")


# Reload the selected file from cogs
@client.command()
@commands.check(is_guild_owner)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Hi, bot owner\n\'{extension}\' is reloaded")


# Load everything in cogs when the client is on
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(
            # Remove the last 3 characters from the file name (".py")
            f"cogs.{filename[:-3]}")


@client.command()
@commands.check(is_guild_owner)
async def owner_test(ctx):
    await ctx.send(f"{ctx.author.mention}, you are the server owner")


@client.event
async def on_command_error(ctx, error):
    if ctx.command.name == "_8ball":
        await ctx.send("Usage: `.8ball <Yes-or-No Question>`")
    elif ctx.command is not None:
        await ctx.send(
            f"{ctx.author.mention}, you do not have permission to this command\n{error}"
        )


# Ping
@client.command(aliases=["p"])
# Command name follow the function name
# A simple command to measure ping in ms
async def ping(ctx):
    await ctx.send(f"Pong! `{round(client.latency * 1000)}ms`")


client.owner_id = os.environ['OWNER_ID']
TOKEN = os.environ['TOKEN']
client.run(TOKEN)
