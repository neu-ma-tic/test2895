from discord.ext import commands
import datetime
import discord
import qrcode
import requests
import os
import random

token = os.environ.get("TOKEN")
bot = commands.Bot(command_prefix='!', help_command=None)


@bot.event
async def on_ready():
    x = datetime.datetime.now().strftime("%H:%M")
    s = str(len(bot.guilds))
    print('====================================')
    print(f'Online                         {x}')
    print('')
    print(f'servers          >>>               {s}')
    print('prefix           >>>               !')
    print('')
    print('        use !help for commands       ')
    print('  Bot Created by Zombiebattler#9961  ')
    print('====================================')
    print(' ')
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing,
                                  name='an sich selbst',
                                  game=discord.Game))


@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"Pong {ctx.message.author}")
    print(f"ping >>> {ctx.message.author}")


@bot.command()
async def website(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Coole webseite",
                          url="https://leonkcom.leonkoelmel.repl.co",
                          description="Nice webseite von mir",
                          color=0xFF5733)
    await ctx.send(embed=embed)
    print(f"website >>> {ctx.message.author}")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="alle befehle",
                          description="(prefix: !)",
                          color=0xFF0000)
    embed.add_field(name="locate <ip adresse>",
                    value="lokalisiere eine ip adresse",
                    inline=False)
    embed.add_field(name="website", value="mein weseite", inline=False)
    embed.add_field(name="ping", value="Testbefehl", inline=False)
    embed.add_field(name="dm", value="sende private naricht", inline=False)
    embed.add_field(name="qr <Link/Text>",value='erstellle ein QR code zu einem link oder text',inline=False)
    embed.add_field(name="dice",value='Würfel eine random zahl',inline=False)
    embed.add_field(name="server",value='server anzahl des bot',inline=False)
    embed.add_field(name="test",value='testbefehl',inline=False)
    await ctx.send(embed=embed)
    print(f"help >>> {ctx.message.author}")


@bot.command()
async def locate(ctx, arg):
    await ctx.send(f"Deine Gesuchte IP {ctx.message.author.mention}")
    response = requests.get(f'http://ip-api.com/json/{arg}').json()
    status = (response['status'])
    embed = discord.Embed(title="", description="", color=0xFFFFFF)
    if status in ['success']:
        embed.add_field(name="IP", value=arg, inline=False)
        embed.add_field(name="Status", value=(response['status']), inline=True)
        embed.add_field(name="Land", value=(response['country']), inline=True)
        embed.add_field(name="Stadt", value=(response['city']), inline=True)
        embed.add_field(name="lat", value=(response['lat']), inline=True)
        embed.add_field(name="lon", value=(response['lon']), inline=True)
        embed.add_field(name="Zeitzone",
                        value=(response['timezone']),
                        inline=True)
        embed.add_field(name="Anbiter", value=(response['as']), inline=True)
    else:
        embed.add_field(name="IP", value=arg, inline=False)
        embed.add_field(name="Status", value=(response['status']), inline=True)
        embed.add_field(name="Naricht",
                        value=(response['message']),
                        inline=True)
    await ctx.send(embed=embed)
    print(f"locate [IP: {arg}] >>> {ctx.message.author} >>> {response['status']}")


@bot.command()
#async def dm(ctx, member: discord.User, *, content):
async def dm(ctx):
    member = ctx.message.author
    content = f'Hallo {ctx.message.author}'
    await member.send(content)
    print(f"dm >>> {ctx.message.author}")


@bot.command()
async def qr(ctx, *, arg):
    data = arg 
    filename = "site.png"
    lol = qrcode.make(data)
    lol.save(filename)
    await ctx.message.delete()
    await ctx.send(f'QR Code for {ctx.message.author}')
    await ctx.send(file=discord.File('site.png')) 
    os.remove('site.png')
    print(f"QR [{arg}] >>> {ctx.message.author}")

@bot.command()
async def dice(ctx, arg = 6):
  zahl = random.randint(1,arg)
  await ctx.send(zahl)
  print(f"Würfel [{zahl}] >>> {ctx.message.author}")


@bot.command()
async def server(ctx):
  server = str(len(bot.guilds))
  await ctx.send(server)


@bot.command()
async def test(ctx):
  await ctx.send("TestBefehl")



bot.run(token)
