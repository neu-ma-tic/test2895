from discord.ext.commands import Cog, Context, command, has_role, guild_only
from discord import Member

from bot import Bot
from utils.checks import has_profile
from utils.roles_id import _officer_

class CPcommands(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @command(name="add-cp")
    @guild_only()
    @has_profile()
    @has_role(_officer_)
    async def add_cp(self, ctx: Context, person: Member, amount: int = 1) -> None:
        embed = await self.bot._add_cp(ctx, person, amount)
        await ctx.send(embed=embed)
    
    @command(name="remove-cp")
    @guild_only()
    @has_profile()
    @has_role(_officer_)
    async def remove_cp(self, ctx: Context, person: Member, amount: int = 1) -> None:
        embed = await self.bot._remove_cp(ctx, person, amount)
        await ctx.send(embed=embed) 
    

def setup(bot: Bot) -> None:
    bot.add_cog(CPcommands(bot))