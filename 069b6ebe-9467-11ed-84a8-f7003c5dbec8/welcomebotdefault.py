import discord
from discord.ext import commands
from discord.ext.commands import Bot
TOKEN = 'TOKEN HERE'
PREFIX = '¡'
INTENTS = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, intents=INTENTS)



@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
@client.event
async def on_member_join(member):
    canal=client.get_channel(818873007853797439)
    embed=discord.Embed(color=0xff2f2f)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/836351509796225035/836353278777229352/oceanorp.png")
    embed.add_field(name="Bienvenido a Oceano RP", value=(f"{member.mention} Bienvenido a Oceano RP y pasatelo bien en nuestro servidor de roleplay!"), inline=True)
    embed.set_footer(text="XYZ Cloud", icon_url="https://cdn.discordapp.com/attachments/746349531087503448/808432645243273236/photos_host.png")
    await canal.send(embed=embed)
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int=None):
    async for msg in ctx.message.channel.history(limit=limit+1):
        await msg.delete()
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def ban(context, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await context.send(f'The user {member} has been banned')
client.run(TOKEN)