"""Discord Bot for SMHS GWC 2021!!!"""
import os

from utils import logger
# :D
import requests
from discord.ext.commands import Bot
import datetime
import pytz

bot = Bot(command_prefix="$", description="SMHS GWC 2021")


# Debug info so we know when our bot is ready to party.
@bot.listen("on_ready")
async def log_on_ready():
    logger.info(f"{bot.user} has connected to Discord!")


# Example 0
@bot.command()
async def speak(ctx):
    """Robot says hello."""
    await ctx.send(":robot: Beep boop. Boop beep.")


# Example 1
@bot.command()
async def echo(ctx, *args: str):
    """Repeat message."""
    # Hint: `args` is a tuple.
    await ctx.send(args)
    await ctx.send(" ".join(args))


# Example 2
@bot.command()
async def add(ctx, *args):
    """Add numbers cuz math is hard."""
    # Hint: `args` are strings, they must be converted to integers to be summed.
    # What happens if we pass something that is not representative of a number?
    
    equation = " + ".join(args)
    
    total = 0
    for num in args:
        total += int(num)

    await ctx.send(f"{equation} = {total}")


# Example 3
@bot.command()
async def fizzbuzz(ctx, num: int):
    """Thowback to the FizzBuzz activity."""
    rtn = ""

    if not num % 3:
        rtn += "Fizz"
    if not num % 5:
        rtn += "Buzz"

    await ctx.send(rtn if rtn else num)


# Example 4
@bot.command()
async def inspiration(ctx):
    """Inspirational quotes provided by https://zenquotes.io/."""
    response = requests.get("https://zenquotes.io/api/random")
    # From the docs, https://zenquotes.io/#docs, the response format is:
    # [ { "q": "<quote>", "a": "<author>", "h": "<html>" } ]
    data = response.json()[0]
    await ctx.send(f"{data['q']} - {data['a']}")

# surprise :D
@bot.command()
async def surprise(ctx):
    """A fantastical surprise."""
    data = ("https://knowyourmeme.com/memes/surprised-pikachu")
    await ctx.send(data)
    

# Valentina 1
@bot.command()
async def minion_speak(ctx, text):
    """banana"""
    from urllib.parse import quote
    url_text = quote(text)
    url = f"https://api.funtranslations.com/translate/minion.json?text={url_text}"
    response = requests.get(url)
    data = response.json()
    translation = data["contents"]["translated"]
    await ctx.send(translation)


# Class Demo
@bot.command()
async def secret(ctx):
    """Tell a secret."""
    data = "https://genius.com/Rick-astley-never-gonna-give-you-up-lyrics"
    await ctx.send(data)

@bot.command()
async def demo2(ctx):
    """Demo2 command"""
    # https://docs.python.org/3/library/datetime.html
    current_time = datetime.datetime.now()
    # TODO: Convert to London TZ
    await ctx.send(current_time)
    #  https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
  

# Carlos adds easter egg. #teehee
@bot.listen('on_message')
async def msg_responses(message):
    # Ignore messages from bot. Otherwise may get stuck in a loop.
    if message.author == bot.user:
        return

    # So actions are case insensitive.
    msg_content = message.content.casefold()

    if msg_content.startswith("lol") or " lol" in msg_content:
        await message.channel.send("#teehee")

    if "teehee" in msg_content:
        await message.add_reaction("\N{Rolling on the Floor Laughing}")


# Maya's Command
@bot.command(name = "timein")
async def time_in(ctx, city):
  # initalizing selected_tz
  selected_tz = ''
  for i in range(0, len(pytz.all_timezones)):
    # making your input lowercase and the list of all the available timezones in pytz lowercase
    if city.lower() in pytz.all_timezones[i].lower():
      selected_tz = pytz.all_timezones[i]
      break
  if selected_tz:
    # sending out actual timezone
    await ctx.send(datetime.datetime.now(tz = pytz.timezone(selected_tz)))
  else:
    # if your timezone is not available in pytz it will print "cannot find time for..."
    await ctx.send("cannot find time for " + city)


# The bot's coroutine
bot.run(os.getenv("API_TOKEN"))
