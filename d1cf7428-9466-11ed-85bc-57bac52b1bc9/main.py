import discord
import os
from discord.ext import commands
from keep_alive import keep_alive


class PurdueHackersBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            description='BoilerBot',
            intents=discord.Intents.default(),
            application_id = os.environ['APPLICATION_ID']
        )
    async def load_extensions(self) -> None: 
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

    async def setup_hook(self) -> None:
        self.remove_command('help')
        await self.load_extensions()
        await bot.tree.sync()

bot = PurdueHackersBot()


keep_alive() # uncomment this line if you want to run the bot on repl.it

bot.run(os.environ['BOT_TOKEN'])
