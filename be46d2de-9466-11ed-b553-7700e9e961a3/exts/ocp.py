from discord.ext.commands import Cog, Context, command, has_role, guild_only
from discord import Member

from bot import Bot
from utils.checks import has_profile
from utils.roles_id import _hicom_

class OCPcommands(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @command(name="add-ocp")
    @guild_only()
    @has_profile()
    @has_role(_hicom_)
    async def add_ocp(self, ctx: Context, person: Member, amount: int = 1) -> None:
        embed = await self.bot._add_ocp(ctx, person, amount)
        await ctx.send(embed=embed)
    
    @command(name="remove-ocp")
    @guild_only()
    @has_profile()
    @has_role(_hicom_)
    async def remove_ocp(self, ctx: Context, person: Member, amount: int = 1) -> None:
        embed = await self.bot._remove_ocp(ctx, person, amount)
        await ctx.send(embed=embed) 
    

def setup(bot: Bot) -> None:
    bot.add_cog(OCPcommands(bot))