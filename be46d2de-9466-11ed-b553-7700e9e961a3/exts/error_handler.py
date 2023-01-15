# Error Handler 
# Made by Tpmonkey

from discord.ext.commands import Cog, Context, errors
from discord import Embed, Colour

from bot import Bot
from utils.checks import (
    HasProfile, NoProfile
)

import logging

log = logging.getLogger(__name__)

class ErrorHandler(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: errors.CommandError) -> None:
        command = ctx.command
        print(errors)

        if hasattr(error, "handled"):
            return

        embed = Embed(
            colour = Colour.dark_red()
        )
        
        if isinstance(error, errors.CommandNotFound):
            return
        elif isinstance(error, errors.CommandOnCooldown):
            embed.title = str(error)
        elif isinstance(error, errors.MissingRole):
            embed.title = ":x: **You don't have the required role to use this command!**"
        elif isinstance(error, HasProfile):
            embed.title = ":x: **You're already have your own profile!**"
        elif isinstance(error, NoProfile):
            embed.title = ":x: **You don't have any profile yet, Type `c!join` to create one!**"
        else:
            embed.title = f":x: **{error}**"
        
        await ctx.send(embed=embed)
        log.debug(
            f"Command {command} invoked by {ctx.message.author} with error "
            f"{error.__class__.__name__}: {error}"
        )

def setup(bot: Bot) -> None:
    bot.add_cog(ErrorHandler(bot))