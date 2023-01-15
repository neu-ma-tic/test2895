import asyncio
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import youtube_dl
import os
from time import sleep
import requests
import config

client = commands.Bot(command_prefix = '/') #преффикс для комманд бота

@client.event

#--------------------------------------------------------------------------------------------------------
#ПРОВЕРКА КОННЕКТА
#--------------------------------------------------------------------------------------------------------

async def on_ready():
	print('Logged on as Nevershine#7777!')

#--------------------------------------------------------------------------------------------------------
#ЧИСТКА ЧАТА
#--------------------------------------------------------------------------------------------------------

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear(ctx, amount = 200):
	await ctx.channel.purge( limit = amount )
	print('[SUCCES] chat was cleared')
#--------------------------------------------------------------------------------------------------------
#КИК
#--------------------------------------------------------------------------------------------------------

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member:discord.Member, *, reason = None):
	channel = client.get_channel(675768656004644866)
	await ctx.channel.purge(limit = 1)
	
	await member.kick(reason = reason)

	
#--------------------------------------------------------------------------------------------------------
#БАН
#--------------------------------------------------------------------------------------------------------

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member:discord.Member, *, reason = None):
	emb = discord.Embed(title = 'User has been banned', color = discord.Color.red())
	channel = client.get_channel(675768656004644866)

	await ctx.channel.purge(limit = 1)

	await member.ban(reason = reason)

	emb.set_author ( name = member.name, icon_url = member.avatar_url)
	emb.add_field ( name = 'Reason: {}'.format(reason) , value = 'Banned user : {}'.format( member.mention ))

	await channel.send( embed = emb)
	
#--------------------------------------------------------------------------------------------------------
#ПРИВЕТУСИЧКИ
#--------------------------------------------------------------------------------------------------------
@client.event
async def on_member_join(member):
	channel = client.get_channel(675431801015107594)
	channel_send = client.get_channel(676803226489716791)
	await channel_send.send(f'Покорный слуга приветствует путника - {member.mention}, проходите в нашу уютную комнату, прочтите правила и выберите свою роль в нашем клане!')
@client.command()
async def txt(ctx, arg):
	await ctx.channel.purge(limit = 1)
	await ctx.send(arg)
#MUSIC
#--------------------------------------------------------------------------------------------------------
@client.command()
async def join(ctx):
    global voice
    channel=ctx.message.author.voice.channel
    voice=get(client.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command()
async def leave(ctx):
	channel = ctx.message.author.voice.channel
	voice = get(client.voice_clients, guild=ctx.guild)
	if voice and voice.is_connected():
		await voice.disconnect()
	else:
		voice = await channel.connect()


client.run(config.TOKEN)