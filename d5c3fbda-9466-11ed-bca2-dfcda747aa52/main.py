#Discord Bot
#To add this bot into a new server, use this: https://discord.com/api/oauth2/authorize?client_id=880879264482881586&permissions=8&scope=bot
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random

TOKEN = os.getenv("API-KEY") #Replace with token

client = commands.Bot(command_prefix='!') #Sets the command prefix for the bot
bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

@bot.event
async def on_message(message): #The instance where a user sends a message

  await bot.process_commands(message)

  if message.author == client.user:
    return
  
  if message.content.startswith('!help'): #Command within on_message
    await message.channel.send("This is the help menu")

@bot.command()
async def example1(ctx): #Command as a function (Type !example1 to use)
  await ctx.send("This is example command 1")
  
@bot.command()
async def Oi(ctx): #Command as a function (Type !Oi U Just Got Caught! to use)
  await ctx.send("Oi! U Just Got Caught!")

@bot.command()
async def rps(ctx, move):
  move = str(move).lower()
  bot_moves = ["rock", "paper", "scissors"]
  choice = random.choice(bot_moves)

  print(choice)
  
  if(move == "rock" and choice == "rock"):
    await ctx.send("It is a draw")
  elif(move == "rock" and choice == "paper"):
    await ctx.send(f"My choice is {choice}. I win!")
  elif(move == "rock" and choice == "scissors"):
    await ctx.send(f"My choice is {choice}. You win!")
  elif(move == "paper" and choice == "rock"):
    await ctx.send(f"My choice is {choice}. You win!")
  elif(move == "paper" and choice == "paper"):
    await ctx.send(f"It is a draw") 
  elif(move == "paper" and choice == "scissors"):
    await ctx.send(f"My choice is {choice}. I win!")
  elif(move == "scissors" and choice == "rock"):
    await ctx.send(f"My choice is {choice}. I win!")
  elif(move == "scissors" and choice == "paper"):
    await ctx.send(f"My choice is {choice}. You win!")
  elif(move == "scissors" and choice == "scissors"):
    await ctx.send(f"It is a draw") 

@bot.event
async def on_ready(): #The instance where the bot is ready
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  print('------')

bot.run(TOKEN) #Runs the bot



