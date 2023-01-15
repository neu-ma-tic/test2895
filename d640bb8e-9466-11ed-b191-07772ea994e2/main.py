import random
import time
import discord
from discord import DMChannel
from discord.ext import commands

def is_it_me(ctx):
    return ctx.author.id == 830419635564314664
note = [""]
DmNumber = ""

client2 = discord.Client()
client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
	print("Bot Is Ready")

@client.command()
@commands.check(is_it_me)
async def Hello(ctx):
	await ctx.send("Hi!!😄😄")

@client.command(aliases=['8ball','Test'])
@commands.has_permissions(manage_messages=True)
async def _8ball(ctx, *, question):
	responses = ("Yes", "No","Maybe")
	await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def Gamble(ctx):
	Winner = ("Black⚫", "White⚪","Red🔴","Blue🔵")
	await ctx.send(f"Winner: {random.choice(Winner)}\nNoice :)")

@client.command()
@commands.has_permissions(manage_messages=True)
async def Spam(ctx, question):
    await ctx.send(f"{question}" * 60)

@client.command(aliases=['purge'])
@commands.check(is_it_me)
async def clear(ctx, question):
	await ctx.channel.purge(limit=int(question))
	await ctx.send(f'Succesfully Deleted {question} Messages Deleted By {ctx.author}')
	if question > 101:
		ctx.send("Sorry Cant Delete More Than 100 Bud 😞😞")

@client.command()
@commands.has_permissions(manage_messages=True)
async def Save_Note(ctx, question, amount=2):
	note[0] = question
	await ctx.send("Succesfully Saved On Note 1😄😁")
	await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(manage_messages=True)
async def Open_Note(ctx):
	await ctx.send(f"Your Note: {note}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def coinflip(ctx):
	HorT = ("Heads", "Tails")
	await ctx.send(f"😄Winner: {random.choice(HorT)} Noice 😁")

@client.command()
@commands.has_permissions(manage_messages=True)
async def Wanna_Join(ctx):
	await ctx .send("Wanna Join Our Game Studio.. Join Us If You Are A Sprite Music Sfx Or A Game Developer You Are Welcome Here😁😀👍😃😆\nhttps://discord.gg/VgBGnPpNpc")

@client.command()
@commands.has_permissions(manage_messages=True)
async def rps(ctx, *, question):
	picks = ("Rock", "Paper", "Siccors")
	await ctx.send(f"Your Pick Is: {picks}\nAnd I Pick: (random.choice{picks})")

@client.command()
@commands.has_permissions(manage_messages=True)
async def WikiSearch(ctx, question):
	await ctx.send(f"https://en.m.wikipedia.org/wiki/{question}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def Fortune(ctx):
    fortune = ["You Became A Millioare", "You Have The Best Pc Set In The World", "You Got A Job At Your Dream Company", "You Have The Best Gaming Phone Ever", "You Became The President Of Your Country", "You Saw A Million Dollar Check"]
    Consequence = ["You Have The Fbi Chasing You", "You Will Be Sent In Jail For 20 Years", "The Police Is After You", "A Hacker Hacked Into Your Pc", "Your Phone Got Smashed", "You Are Being Targeted"]
    await ctx.send(f"Fortune: {random.choice(fortune)} YES!!😆😄🤩\n But:{random.choice(Consequence)} Oh No!😱😰\nYou Take It?")
async def Yes(ctx):
    yes = 0
    yes += 5
    await ctx.send("Ok Votes{yes}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def Devlog1(ctx):
    await ctx.send("Of Course And Please Subsciribe")
    time.sleep(0.5)
    await ctx.send("https://youtu.be/hb1td_mEfN8")

@client.command()
@commands.has_permissions(manage_messages=True)
async def GameBeta(ctx):
    await ctx.send("https://synxgamedev.itch.io/rooftop-dasher-beta")
    await ctx.send("Its For Beta Testers Only")

@client.command()
@commands.has_permissions(manage_messages=True)
async def YtSearch(ctx, *, question):
    await ctx.send(f"You Searched For: {question}\nResult: https://m.youtube.com/results?sp=mAEA&search_query={question}")

@client.command(name='dmsend', pass_context=True)
async def dmsend(ctx):
    user = await client.fetch_user("817134155912577085")
    await DMChannel.send(user, "***System*** ***Unlocked***")
    time.sleep(0.5)
    await DMChannel.send(user, "Trying To Acces System...." * 50)
    time.sleep(2)
    await DMChannel.send(user, "10 101 010 1" * 100)
    time.sleep(5)
    await DMChannel.send(user,"*Acces Granted*")
    time.sleep(5)
    await DMChannel.send(user, " ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■ ■■")
    await DMChannel.send(user,"C∅p¥īñG Ælllllll Flliileeess")
    await DMChannel.send(user, "Creating Folder Now......")
    await DMChannel.send(user, "Completed Wed:July:2021 ends in 6:49:40..")
    time.sleep(5)
    await DMChannel.send(user, "https://z0r.de/" * 100)
    await DMChannel.send(user, "http://wwwwwwwww.jodi.org/" * 100)
    await DMChannel.send(user, "Boohbah.tv" * 100)
    

#DocumentPages
@client.command()
async def DocumentPage1(ctx):
    await ctx.send("@Ælluminati's stement#1: Falingo is A Filipino")

@client.command()
async def DocumentPage2(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage3(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage4(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage5(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage6(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage7(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage8(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage9(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage10(ctx):
    await ctx.send("***Nothing Yet***")

@client.command()
async def DocumentPage11(ctx):
    await ctx.send("***IT ONLY HAS 10 PAGES IDIOT***")

@client.command()
async def DTUBE(ctx, *, amount=2):
    await ctx.send("Opening Dtube")
    await ctx.send("Pls Wait Its Loading...")
    time.sleep(2)
    await ctx.send("""
    **DOLPHIN TUBE**
    | 
    |
    |     (╯°□°） \\**TRENDING**// (╯°□°）
    |
    |---------------------------------------- 
    | TITLE: Dolphin  HUG
    | DESCRIPTION: A Girl Hug With A Dolphin
    | Command:{>Dtube1}
    |----------------------------------------
    |---------------------------------------- 
    | TITLE: Petting Cat
    | DESCRIPTION: August 69 2021
    | Command:{>Dtube2}
    |----------------------------------------
    |---------------------------------------- 
    | TITLE: Kissers HAHA (Badboy Dolphie)
    | DESCRIPTION: Kiss em bitches
    | Command:{>Dtube3}
    |----------------------------------------
    |---------------------------------------- 
    | TITLE:
    | DESCRIPTION:
    | Command:{>Dtube}
    |----------------------------------------
    |---------------------------------------- 
    | TITLE:
    | DESCRIPTION:
    | Command:{>Dtube}
    |----------------------------------------
    |.     You Have Reached The End.         
    |""")

@client.command()
async def Dtube1(ctx):
    await ctx.send("https://c.tenor.com/M2xu1XHeBVsAAAAM/hugs-dolphin.gif")

@client.command()
async def Dtube2(ctx):
    await ctx.send("https://c.tenor.com/G0QafTDu7ewAAAAM/cat-dolphin.gif")

@client.command()
async def Dtube3(ctx):
    await ctx.send("https://c.tenor.com/_9ADndk7HPwAAAAM/dolphin-kiss.gif")

@client.command()
async def CloseGif(ctx, *, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def DtubeHelp(ctx):
    await ctx.send("(DTUBE)-Open Dtube (CloseGif)-Close Video (Dtube(number)-Open Video [EASY COMMANDS]")

@client.command()
async def DuploadHelp(ctx):
    await ctx.send("Add A Title A Video Link And A Description... Do [>Title: (Title) Video:(Video Link) and Description:(Description)] ")

@client.command()
async def Dupload(ctx):
    await ctx.send("Uploading Pls Wait A Few Minutes Till It Is Uploaded Thanks....")
    await ctx.send("1%")
    time.sleep(5)
    await ctx.send("2%")
    time.sleep(5)
    await ctx.send("3%")
    time.sleep(5)
    await ctx.send("4%")
    time.sleep(5)
    await ctx.send("5%")
    time.sleep(5)
    await ctx.send("6%")
    time.sleep(5)
    await ctx.send("7%")
    time.sleep(5)
    await ctx.send("8%")
    time.sleep(5)
    await ctx.send("9%")
    time.sleep(5)
    await ctx.send("10%")
    time.sleep(5)
    await ctx.send("11%")
    time.sleep(5)
    await ctx.send("12%")
    time.sleep(5)
    await ctx.send("13%")
    time.sleep(5)
    await ctx.send("14%")
    time.sleep(5)
    await ctx.send("15%")
    time.sleep(5)
    await ctx.send("16%")
    time.sleep(5)
    await ctx.send("17%")
    time.sleep(5)
    await ctx.send("18%")
    time.sleep(5)
    await ctx.send("19%")
    time.sleep(5)
    await ctx.send("20%")
    time.sleep(5)
    await ctx.send("21%")
    time.sleep(5)
    await ctx.send("22%")
    time.sleep(5)
    await ctx.send("23%")
    time.sleep(5)
    await ctx.send("24%")
    time.sleep(5)
    await ctx.send("25%")
    time.sleep(5)
    await ctx.send("26%")
    time.sleep(5)
    await ctx.send("27%")
    time.sleep(5)
    await ctx.send("28%")
    time.sleep(5)
    await ctx.send("29%")
    time.sleep(5)
    await ctx.send("30%")
    time.sleep(5)
    await ctx.send("31%")
    time.sleep(5)
    await ctx.send("32%")
    time.sleep(5)
    await ctx.send("33%")
    time.sleep(5)
    await ctx.send("34%")
    time.sleep(5)
    await ctx.send("35%")
    time.sleep(5)





embedmess = ""

@client.command()
@commands.check(is_it_me)
async def NewPoll(ctx, question):
    embedmess = question
    await ctx.channel.purge(limit=1)
    await ctx.send("@everyone @here")
    embed = discord.Embed(
    title = "@everyone NEW POLL!!!", description = f"```{embedmess}```", color = discord.Colour.random())
    embed.add_field(name=f"Requested By: ", value = ctx.author)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("☑️")

@client.command()
async def Need(ctx, question):
  await ctx.send(question * 50)


client.run('ODU3NTU5NzgwMjk4MDYzODky.YNRWyA.NCUngLaxZWamZxcCKXZjdifccw8')