import asyncio
# import requests
import json
import random
import sqlite3
import time
import typing
from datetime import datetime

import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot

Token = "OTU4MDc5NjU1NDE4NjYyOTUy.G1_Sx-.EKUTzEtu0aedSGHf9ZvPQGPlgWkuG0WzjsY6Sk"
bot = commands.Bot(command_prefix='!')
bot.remove_command("help")
prefix = '!'
mainchannel = bot.get_channel(872640765149462561)
logged_at = datetime.now()
conn = sqlite3.connect("users.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS USERS (perm text, user text)""")
c.execute("""CREATE TABLE IF NOT EXISTS ADMIN (prefix text, user text)""")
c.execute(
    """CREATE TABLE IF NOT EXISTS CHECKLIST (member text, checks text)""")
t = []
fi = []
fa = []
fb = False


def update_table(table, perm, userr, search1, search2):
    if table == 'ADMIN':
        c.execute(
            f"""UPDATE {table} SET prefix = '{perm}', user = '{userr}' WHERE prefix = '{search1}' AND user = '{search2}'"""
        )
        conn.commit()
        c.execute("SELECT * FROM {0}".format(table))
        t = c.fetchall()
        return (t)
    if table == 'USERS':
        c.execute(
            f"""UPDATE {table} SET perm = '{perm}', user = '{userr}' WHERE perm = '{search1}' AND user = '{search2}'"""
        )
        conn.commit()
        c.execute("SELECT * FROM {0}".format(table))
        t = c.fetchall()


def select(table,
           table_value=None,
           value=None,
           all=None,
           count=None,
           total_all=None):
    global fa
    if all == None:
        c.execute("SELECT {0} FROM {1} WHERE{2}='{2}'".format(
            count, table, table_value, value))
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
        c.execute(
            f"SELECT * FROM {table} WHERE perm='{perm}' AND user='{user}'")
        fa = c.fetchall()
        if fa == fi:
            fb = False
            return (False)
        if fa != fi:
            fb = True
            return (True)
    if sfuo == True:
        c.execute(f"SELECT * FROM {table} WHERE user='{user}'")
        fa = c.fetchall()
        if fa == fi:
            fb = False
            return (False)
        if fa != fi:
            fb = True
            return (True)


def update_admin(table, perm, userr, search1, search2):
    c.execute(
        f"""UPDATE {table} SET perm = '{perm}', user = '{userr}' WHERE perm = '{search1}' AND user = '{search2}'"""
    )
    conn.commit()
    c.execute("SELECT * FROM {0}".format(table))
    print(c.fetchall())


# def get_quote():
#   response = requests.get('https://zenquotes.io/api/random')
#   json_data = json.loads(response.text)
#   quote = json_data[0]['q'] + ' \n-' + json_data[0]['a']
#   return(quote)


@bot.event
async def on_ready():
    mainchannel = bot.get_channel(860239294093066263)
    #   Has to be in the same command/event to be able to send idkw
    await mainchannel.send('Logged In at' + ' ' + logged_at.strftime('%I:%M'))
    print('Bot Logged as BBC', ' ', str(mainchannel))


# Logging the bot activated Message in discord


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            f'Command Does Not exist Use {prefix}help to find a list of all commands and what they do'
        )


@bot.command()
async def add_admin(ctx, table, user: typing.Union[discord.TextChannel,
                                                   discord.Member]):
    global fb
    fh = ctx.author
    find_userin_admin("USERS", fh, False, 'Admin')
    if ctx.author.name == 'Hentai Papa' and ctx.author.discriminator == '1931':
        c.execute("INSERT INTO {0} VALUES ('Admin', '{1}')".format(
            table, user))
        conn.commit()
        await ctx.send(f'Added {user} Into Database')
        return
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        c.execute("INSERT INTO {0} VALUES ('Admin', '{1}')".format(
            table, user))
        conn.commit()
        await ctx.send(f'Added {user} Into Database')


# (table, user, sfuo=False, perm=None):
@bot.command()
async def ss(ctx, *, member: typing.Union[discord.TextChannel,
                                          discord.Member]):
    global fb
    fh = member
    find_userin_admin("USERS", fh, False, 'Admin')
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

# @bot.command()
# async def getquote(ctx):
#     quotee = get_quote()
#     await ctx.channel.purge(limit=1)
#     await ctx.send(quotee)


@bot.command()
async def clear(ctx, amount: int):
    global fb
    fh = ctx.author
    find_userin_admin("USERS", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        await ctx.channel.purge(limit=amount)


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    global fb
    fh = ctx.author
    find_userin_admin("USERS", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention} for \'{reason}\' ')


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    global fb
    fh = ctx.author
    find_userin_admin("USERS", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention} for \'{reason}\' ')


@bot.command()
async def unban(ctx, *, member):
    global fb
    fh = ctx.author
    find_userin_admin("USERS", fh, False, 'Admin')
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


# @bot.command()
# async def help(ctx, *, page):
#     if page == 1:
#         await ctx.send('```diff\n-Help Menyu')


@bot.command()
async def select_table(ctx, *, table):
    c.execute(f"SELECT * FROM {table}")
    await ctx.send(c.fetchall())


#Don't Do conn.close()
@bot.command()
async def Update_table(ctx, table, perm,
                       user: typing.Union[discord.TextChannel, discord.Member],
                       search1, search2: typing.Union[discord.TextChannel,
                                                      discord.Member]):
    global fb
    fh = ctx.author
    find_userin_admin("USERS", fh, False, 'Admin')
    if ctx.author.name == 'Hentai Papa' and ctx.author.discriminator == '1931':
        await ctx.send('Updating...')
        c.execute(f"SELECT * FROM {table}")
        await ctx.send(c.fetchall())
        c.execute(
            f"UPDATE {table} SET perm = '{perm}', user='{user}' WHERE perm = '{search1}' AND user = '{search2}'"
        )
        conn.commit()
        c.execute(f"SELECT * FROM {table}")
        await ctx.send(c.fetchall())
        await ctx.send('Done')
        return
    if fb == False:
        await ctx.send(f'You Don"t Have Permission To Use This Command')
    if fb == True:
        await ctx.send('Updating...')
        c.execute(f"SELECT * FROM {table}")
        await ctx.send(c.fetchall())
        c.execute(
            f"UPDATE {table} SET perm = '{perm}', user='{user}' WHERE perm = '{search1}' AND user = '{search2}'"
        )
        conn.commit()
        c.execute(f"SELECT * FROM {table}")
        await ctx.send(c.fetchall())
        await ctx.send('Done')


count = 0


@bot.command()
async def timer(ctx, limit: int):
    count = 0
    message = await ctx.send("Timer: {0}".format(count))
    while count < limit:
        await asyncio.sleep(1)
        count += 1
        await message.edit(content="Timer: {0}".format(str(count)[0:5]))
        if count == limit:
            break


@bot.command()
async def Help(ctx, page: typing.Optional[int] = 4):
    if page == 1:
        await ctx.send(
            '```diff\nHelp 1\n-No Permission Commands:\n-bottles {number betweem 1 and 100; Not Required} {liquid; Not Required}\n-say {message} Type What you want to say And the Bot Will say It \n-say2 {Message} A Beta Version of say\n-slap {User} {Reason} Slaps A User\n-ss {user} checks if a user is a Admin  \n-timer {time} A Timer   \n-union {user} gets a users name fakeuser#0001 instead of @fakeuser If They Are In the Server\nDo Help 2 To Go To The Next page```'
        )
    if page == 2:
        await ctx.send(
            "```diff\nHelp 2\n-Admin Commands:\n-add_admin {table;Required} {user;Required} Adds A Admin   \n-ban {user} {reason} Ban's a User Reason not Required          \n-clear {limit} Deletes Messages with a Limit\n-kick {user} {reason} Kicks A User Reason is Not Required           \n-ss {user} checks if a user is a Admin\nDo Help 3 To Go To The Next page```"
        )
    if page == 3:
        await ctx.send(
            "```diff\nHelp 3\n-All Commands:\n-add_admin {table;Required} {user;Required} Adds A Admin   \n-ban {user} {reason} Ban's a User Reason not Required          \n-bottles {number betweem 1 and 100; Not Required} {liquid; Not Required}      \n-clear {limit} Deletes Messages with a Limit        \n-kick {user} {reason} Kicks A User Reason is Not Required         \n-say {message} Type What you want to say And the Bot Will say It          \n-say2 {Message} A Beta Version of say         \n-select_table {table} Returns Every Value From A Table \n-slap {User} {Reason} Slaps A User         \n-ss {user} checks if a user is a Admin           \n-timer {time} A Timer         \n-unban {user} Unban's A User        \n-union {user} gets a users name fakeuser#0001 instead of @fakeuser If They Are In the Server       \n-update_table {table} {perm} {user} {search_perm} {search_user} Updates A Table And Its Propertys\nGo To https://www.myinfo.com/BBC/184132 For more info```"
        )
    if page == 4:
        await ctx.send(
            '```diff\nHelp 1\n-No Permission Commands:\n-bottles {number betweem 1 and 100; Not Required} {liquid; Not Required}\n-say {message} Type What you want to say And the Bot Will say It \n-say2 {Message} A Beta Version of say\n-slap {User} {Reason} Slaps A User\n-ss {user} checks if a user is a Admin  \n-timer {time} A Timer   \n-union {user} gets a users name fakeuser#0001 instead of @fakeuser If They Are In the Server\nDo Help 2 To Go To The Next page```'
        )


@bot.command()
async def help(ctx, page: typing.Optional[int] = 4):
    if page == 1:
        await ctx.send(
            '```diff\nHelp 1\n-No Permission Commands:\n-bottles {number betweem 1 and 100; Not Required} {liquid; Not Required}\n-say {message} Type What you want to say And the Bot Will say It \n-say2 {Message} A Beta Version of say\n-slap {User} {Reason} Slaps A User\n-ss {user} checks if a user is a Admin  \n-timer {time} A Timer   \n-union {user} gets a users name fakeuser#0001 instead of @fakeuser If They Are In the Server\nDo Help 2 To Go To The Next page```'
        )
    if page == 2:
        await ctx.send(
            "```diff\nHelp 2\n-Admin Commands:\n-add_admin {table;Required} {user;Required} Adds A Admin   \n-ban {user} {reason} Ban's a User Reason not Required          \n-clear {limit} Deletes Messages with a Limit\n-kick {user} {reason} Kicks A User Reason is Not Required           \n-ss {user} checks if a user is a Admin\nDo Help 3 To Go To The Next page```"
        )
    if page == 3:
        await ctx.send(
            "```diff\nHelp 3\n-All Commands:\n-add_admin {table;Required} {user;Required} Adds A Admin   \n-ban {user} {reason} Ban's a User Reason not Required          \n-bottles {number betweem 1 and 100; Not Required} {liquid; Not Required}      \n-clear {limit} Deletes Messages with a Limit        \n-kick {user} {reason} Kicks A User Reason is Not Required         \n-say {message} Type What you want to say And the Bot Will say It          \n-say2 {Message} A Beta Version of say         \n-select_table {table} Returns Every Value From A Table \n-slap {User} {Reason} Slaps A User         \n-ss {user} checks if a user is a Admin           \n-timer {time} A Timer         \n-unban {user} Unban's A User        \n-union {user} gets a users name fakeuser#0001 instead of @fakeuser If They Are In the Server       \n-update_table {table} {perm} {user} {search_perm} {search_user} Updates A Table And Its Propertys\nGo To https://www.myinfo.com/BBC/184132 For more info```"
        )
    if page == 4:
        await ctx.send(
            '```diff\nHelp 1\n-No Permission Commands:\n-bottles {number betweem 1 and 100; Not Required} {liquid; Not Required}\n-say {message} Type What you want to say And the Bot Will say It \n-say2 {Message} A Beta Version of say\n-slap {User} {Reason} Slaps A User\n-ss {user} checks if a user is a Admin  \n-timer {time} A Timer   \n-union {user} gets a users name fakeuser#0001 instead of @fakeuser If They Are In the Server\nDo Help 2 To Go To The Next page```'
        )


@bot.command()
async def say2(ctx, *args):
    await ctx.send(args)


@bot.command()
async def union(ctx, what: typing.Union[discord.TextChannel, discord.Member]):
    await ctx.send(what)


@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))


@bot.command()
async def slap(ctx,
               members: commands.Greedy[discord.Member],
               *,
               reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))


@bot.command()
async def glians(ctx):
    await ctx.send('https://www.youtube.com/watch?v=US-k_TYQWsg')


bot.run(Token)
