from discord.ext import commands
from discord.ext.commands import Cog

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot