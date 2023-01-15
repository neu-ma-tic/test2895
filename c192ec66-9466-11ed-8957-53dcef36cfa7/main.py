"""
Copyright (c) Baz 2021 Pogchamp - Pog bot for discord
"""

import discord
import json
from itertools import cycle
from discord.ext import commands, tasks
from colorama import Fore
import os
from keep_alive import keep_alive
from datetime import datetime
from random import choice, randint
import asyncio

__version__ = "1.0.0"


client = commands.Bot(command_prefix=commands.when_mentioned_or("pog"))
client.remove_command("help")

status = cycle(["Bot is being re-worked", "IMPORTANT MESSAGE | JOIN SUPPORT SERVER $help", "Commands will NOT work", "Welcome to Pogchamp Restart!", f"pogrob | I just got {randint(0, 1000000)} from robbing the bank!"])

@tasks.loop(seconds=600)
async def change_status():
	await client.change_presence(activity=discord.Game(next(status)))
	print(Fore.GREEN + "Successfully changed status!")

now = datetime.now()

boot_time = now.strftime("%H:%M:%S")

@client.event
async def on_ready():
  print(Fore.BLUE + 'Successfully booted {0.user}'.format(client))
  print("Booted at", boot_time)
  change_status.start()
  await asyncio.sleep(2)
  for guild in client.guilds:
    print(guild.name)
    print(guild.member_count)
    print("-----------------")
    await asyncio.sleep(1)

@client.event
async def on_guild_join(guild):
	print(Fore.GREEN + f"I have joined {guild}")
	print(Fore.RESET)
	for channel in guild.text_channels:
		if channel.permissions_for(guild.me).send_messages:
			await channel.send(f":mailbox:Hi there!:mailbox:\n\n:exclamation:I am Pogchamp - a bot created by Baz!:exclamation:\n\n:incoming_envelope:You can join my support server by running $help or if discord is down, ! andcontact  you can view all of my commands here as well!:incoming_envelope:\n\n:partying_face:Have fun!:partying_face:\n\n\n:information_source:When you added this bot, itas in version {__version__}:information_source:")
		break

@client.event
async def on_guild_remove(guild):
	print(Fore.GREEN + f"I have left {guild}")
	print(Fore.RESET)


@client.command()
async def help(ctx):
  await ctx.send("Need some help or want more info on Pogchamp Restart?\nJoin my support server here!\nhttps://discord.gg/9VC3zYPYps\n\nUse the command prefix\nOr, contact bazthedev@gmail.com! `pog`\n\nhelp\nservers\ninvite\nrob\n\nMore Commands will be added back soon!")

@client.command()
async def invite(ctx):
  await ctx.send(f"{ctx.author.mention} invite my with this link!\nhttps://discord.com/api/oauth2/authorize?client_id=804355903452479489&permissions=3423063233&redirect_uri=https%3A%2F%2Fdiscord.gg%2F9VC3zYPYps&response_type=code&scope=identify%20email%20bot")

@client.command()
async def servers(ctx):
	await ctx.send(f"Currently being pog in **{len(client.guilds)}** servers!")

@client.command()
async def rob(ctx):
  outcomes = [f"Wow! You hit the jackpot and scored ${randint(10000, 100000)}!", "Oof! You were shot in the back and died cos why not", f"Noice! You hacked a small amount of ${randint(100, 10000)}", "You arrived at the bank and was too late because megamind beat you too it", f"You lucky boi! You managed to score ${randint(10, 1000)} cos the bank was explosioned", f"Oh, you died and lost ${randint(1000, 1000000)}", f"You were on your way to the bank, and found a $1 on the floor, so bought a lotto ticket and won ${randint(100000, 1000000000000)} cos your a lucky `person`", "Because of a `reason`, you won $69420"]
  score = await ctx.send(f"{ctx.author.mention} is going to rob the bank!")
  await asyncio.sleep(5)
  await score.edit(content=choice(outcomes))

@client.command()
async def gies(ctx):
  poggies = ["yes very", "ha ha no"]
  await ctx.send(choice(poggies))


@client.command()
async def pp(ctx):
  await ctx.send(f"{ctx.author.mention}\nYour pp is {randint(0, 100)}% larger than the average size!")

keep_alive()
client.run(os.getenv("TOKEN"))