import sqlite3
import random
from datetime import datetime
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import utils
import requests
import json

Token = "OTU4MDc5NjU1NDE4NjYyOTUy.G1_Sx-.EKUTzEtu0aedSGHf9ZvPQGPlgWkuG0WzjsY6Sk"
bot = commands.Bot(command_prefix='!')
prefix = '!'
mainchannel = bot.get_channel(872640765149462561)
logged_at = datetime.now()
conn = sqlite3.connect("users.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS USERS (username text, password text, id int)""")
c.execute("""CREATE TABLE IF NOT EXISTS ADMIN (prefix text, user text)""")
def add_admin(value):
    c.execute("INSERT INTO ADMIN VALUES ('Admin', '{0}')".format(value))
    conn.commit()
fi = []
fa = []
fb = False
def select(table, table_value=None, value=None, all=None, count=None, total_all=None):
    global fa
    if all == None:
        c.execute("SELECT {0} FROM {1} WHERE{2]='{2}'".format(count, table, table_value, value))
        fa = c.fetchall()
def selectall(table, ctx):
    global fa
    c.execute("SELECT * FROM {0}".format(table))
    fa = c.fetchall()
    print(fa)
    ctx.send(fa)
def find_userin_admin(table, user, sfuo=False, perm=None):
    global fi
    global fb
    if sfuo == False:
        c.execute(f"SELECT * FROM {table} WHERE prefix='{perm}' AND user='{user}'")
        fa = c.fetchall()
        if fa == fi:
            fb = False
            return(False)
        if fa != fi:
            fb = True
            return(True)
    if sfuo == True:
        c.execute(f"SELECT * FROM {table} WHERE user='{user}'")
        fa = c.fetchall()
        if fa == fi:
            fb = False
            return(False)
        if fa != fi:
            fb = True
            return(True)


def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' \n-' + json_data[0]['a']
  return(quote)

@bot.event
async def on_ready():
    mainchannel = bot.get_channel(860239294093066263)
#   Has to be in the same command/event to be able to send idkw
    await mainchannel.send('Logged In at' + ' ' + logged_at.strftime('%I:%M'))
    print('Bot Logged as BBC')
# Logging the bot activated Message in discord

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send(f'Command Does Not exist Use {prefix}help to find a list of all commands and what they do')
@bot.command()
async def add_admin(ctx, *, user):
    global fb
    fh = ctx.author
    find_userin_admin("ADMIN", fh, False, 'Admin')
    if ctx.author == 'Hentai Papa#1931':
        c.execute("INSERT INTO ADMIN VALUES ('Admin', '{0}')".format(user))
        conn.commit()
        await ctx.send(f'Added {user} Into Database')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        c.execute("INSERT INTO ADMIN VALUES ('Admin', '{0}')".format(user))
        conn.commit()
        await ctx.send(f'Added {user} Into Database')
# (table, user, sfuo=False, perm=None):
@bot.command()
async def ss(ctx):
    global fb
    fh = ctx.author
    find_userin_admin("ADMIN", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'User {fh} Not In Database')
    if fb == True:
        await ctx.send(f'User {fh} In Database')
@bot.command()
async def say(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    await ctx.send(arg)
# Has to be
#   Double Indented

@bot.command()
async def getquote(ctx):
    quotee = get_quote()
    await ctx.channel.purge(limit=1)
    await ctx.send(quotee)

@bot.command()
async def clear(ctx, amount : int):
    global fb
    fh = ctx.author
    find_userin_admin("ADMIN", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        await ctx.channel.purge(limit=amount)

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    global fb
    fh = ctx.author
    find_userin_admin("ADMIN", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} for \'{reason}\' ')
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    global fb
    fh = ctx.author
    find_userin_admin("ADMIN", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for \'{reason}\' ')

@bot.command()
async def unban(ctx, *, member):
    global fb
    fh = ctx.author
    find_userin_admin("ADMIN", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
  
        for ban_entry in banned_users:
            user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@bot.command()
async def select_allTABLE(ctx, *, table):
    c.execute(f"SELECT * FROM {table}")
    await ctx.send(c.fetchall())
#Don't Do conn.close()
bot.run(Token)