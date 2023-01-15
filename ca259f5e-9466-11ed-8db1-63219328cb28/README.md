# Discord Bot

![Discord Logo](https://droplr.com/wp-content/uploads/2020/06/iconfinder_discord_2308078-512x400.png)

## Architecture

**Discord Guild** < --- > **Bot/Replit.com** < --- > **HTTP API Endpoint**

From Discord we send commands to our bot running on Replit.com. It can make API calls for us and send the answer back to Discord.

## The Setup

This was done ahead of time:

1. Create bot in Discord's Developer Portal, https://discord.com/developers.
![Build-A-Bot](https://files.realpython.com/media/discord-bot-add-bot.4735c88ff16b.png)
1. A secret token will be provide for us to use in our code. This is how the bot knows we are allowed to talk to it.
1. We need to set what permissions we want the bot to have (but not Admin permissions!).
![](https://files.realpython.com/media/discord-bot-scopes.ee333b7a5987.png)
1. We need to add our bot to our guild.

(If you are curious about the specifics, see the reference links at the bottom.)

## discord.py
A 3rd party library that implements the Discord API in Python and adds helpers for bot creation. (Yay, open source tools making things easier for us!)

```py
import discord
```

* Documentation: https://discordpy.readthedocs.io
* Source Code: https://github.com/Rapptz/discord.py

### discord.py Bot
> The creation of bots ... can be daunting and confusing to get correctly the first time. Many times there comes a repetition in creating a bot command framework that is extensible, flexible, and powerful. For this reason, discord.py comes with an extension library that handles this for you.

-- https://discordpy.readthedocs.io/en/latest/ext/commands/

```py
from discord.ext.commands import Bot

bot = Bot("$")
...
bot.run(os.getenv("API_TOKEN"))
```

Represents a discord bot.

Documentation:
  * https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#bots

### Bot commands

> Commands are defined by attaching it to a regular Python function.
A command must always have at least one parameter, `ctx`, which is the Context.
This parameter gives you access to something called the “invocation context”. Essentially all the information you need to know how the command was executed.

```py
@bot.command()  # A shortcut decorator that adds the function to the internal command list.
async def speak(ctx):
    """Robot says hello."""
    await ctx.send(":robot: Beep boop. Boop beep.")
```

Documentation:
  * [Commands](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html)
  * [Commands - Invocation Context](https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#invocation-context)
  * [Bot - Context](https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Context)
  * [Bot - Command Decorator](
https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.GroupMixin.command)

## Computer Sciency Stuff

### Coroutines

As far as we are concerned, it will act like an infinite loop, so we can interact with the bot.

☝️🧐 Remeber that loops are a form of "flow control" in a program? Well, so are coroutines.

```py
bot.run(os.getenv("API_TOKEN"))
```

> multitasking, by allowing execution to be suspended and resumed

-- https://en.wikipedia.org/wiki/Coroutine

> A coroutine is a function that must be invoked with **await** or yield from. When Python encounters an await it stops the function’s execution at that point and works on other things until it comes back to that point and finishes off its work. This allows for your program to be doing multiple things at the same time without using threads or complicated multiprocessing.

-- https://discordpy.readthedocs.io/en/latest/faq.html#coroutines

### Python Decorators

TL;DR: A wrapper to put our function inside of another function. This helps to simplify the code we have to write.

(The big brain term is "closure".)

#### Closure Example

```py
>>> def outer_func(who):
...     name = who.title()
...     def inner_func():
...         return f"Hello, {name}!"
...     return inner_func()
...

>>> print(outer_func("world"))
Hello, World!
```

#### Decorator Example

```py
>>> def add_messages(func):
...     def _add_messages():
...         print("This is my first decorator")
...         func()
...         print("Bye!")
...     return _add_messages
...

>>> @add_messages
... def greet():
...     print("Hello, World!")
...

>>> greet()
This is my first decorator
Hello, World!
Bye!

```

## The other files with the code

### .env

`.env` lets us define environment variables. Replit loads this file automaticly for us. This is a good way to keep secrets, like API tokens, out of our code.


```text
# .env
API_USERNAME=my_cool_handle
```

```py
# main.py
import os
print(os.environ["API_USERNAME"])
```

Replit's docs, https://docs.replit.com/repls/secret-keys.

### project.toml

_**An implementation detail we can ignore for today.**_

TL;DR: It can contain metadata about our code. And it can hold configurations for tools that help manage our code.

### Poetry

_**An implementation detail we can ignore for today.**_

[Poetry](https://python-poetry.org/) turns our code into an installable package and manages any needed dependencies. (It uses the `pyproject.toml` to store its configuration.)

Poetry is gaining popularity, but is not the traditional tool used for this; it  is what Replit has chosen to use.

## Discord Bot Guides

* https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
* https://realpython.com/how-to-make-a-discord-bot-python/
