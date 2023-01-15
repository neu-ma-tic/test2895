# Crusader Profile Manager
# Made by Tpmonkey

from discord.ext.commands import (
    Cog, Context, command, guild_only, cooldown
)
from discord import Member, Embed, Colour

from bot import Bot
from utils.checks import has_no_profile, has_profile
from utils.roles_id import (
    cp_lv_to_id, ocp_lv_to_id
)
from utils.manager import get_data, create_profile, delete_profile, check


class CrusaderProfile(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    
    @command(name="profile", aliases = ("p", "stats", "stat"))
    @cooldown(rate=2, per=10)
    @has_profile()
    @guild_only()
    async def profile(self, ctx: Context, user: Member = None) -> None:
        if user is None:
            user = ctx.author
        
        if not check(user.id):
            await ctx.send(":x: **That user doesn't have any profile at the moment!**")
            return
        
        await self.bot.update_role(ctx)
        ret = get_data(user.id)
        embed = Embed(
            colour = Colour.gold(),
            timestamp = ctx.message.created_at
        )
        pp = ret['data'] # pp means personal profile, not that pp!
        

        embed.set_author(name = f"{user.nick} Crusader Profile", icon_url = user.avatar_url)
        rank = self.bot.get_role(ctx, cp_lv_to_id[pp['cp-lv']])
        rank_name = "Unranked" if rank is None else rank.name
        cp = self.bot.to_number(pp['cp'])
        embed.description =  f"**Rank:** {rank_name}\n**Crusader Points:** {cp}"

        embed.set_footer(text = "Still not finish yet!")
        await ctx.send(embed=embed)
    
    @command(name="oprofile", aliases = ("op", "ostats", "ostat"))
    @cooldown(rate=2, per=10)
    @has_profile()
    @guild_only()
    async def oprofile(self, ctx: Context, user: Member = None) -> None:
        if user is None:
            user = ctx.author

        if not check(user.id):
            await ctx.send(":x: **That user doesn't have any profile at the moment!**")
            return
        
        await self.bot.update_role(ctx)
        ret = get_data(user.id)
        embed = Embed(
            colour = Colour.gold(),
            timestamp = ctx.message.created_at
        )
        pp = ret['data'] # pp means personal profile, not that pp!
        
        embed.set_author(name = f"{user.nick} Officer Crusader Profile", icon_url = user.avatar_url)
        rank = self.bot.get_role(ctx, ocp_lv_to_id[pp['ocp-lv']])
        rank_name = "Unranked" if rank is None else rank.name
        ocp = self.bot.to_number(pp['ocp'])
        embed.description =  f"**Rank:** {rank_name}\n**Officer Crusader Points:** {ocp}"

        embed.set_footer(text = "Still not finish yet!")
        await ctx.send(embed=embed)

    @command(name="join", aliases=("create", ))
    @cooldown(rate=1, per=60)
    @has_no_profile()
    @guild_only()
    async def _create_profile(self, ctx: Context) -> None:
        
        ret = await create_profile(ctx.author.id)
        if ret["success"]:
            await ctx.send("Created your profile.")
            await self.bot.update_role(ctx)
        else:
            await ctx.send(":x: **Unable to create a profile, Please try again later!**")
    
    @command(name="update")
    @cooldown(rate=1, per=60)
    @guild_only()
    @has_profile()
    async def update(self, ctx: Context) -> None:
        await self.bot.update_role(ctx)
        await ctx.send("**Updated your roles.**")

    
    @command(name="delete")
    @cooldown(rate=1, per=3600)
    @has_profile()
    @guild_only()
    async def delete_char(self, ctx: Context) -> None:
        mess = await ctx.send(f"Type `{ctx.author.nick}` in 15 seconds to confirm!")
        try:
            m = await self.bot.wait_for_message(ctx, timeout=15)
        except:
            await mess.edit(content="Canceled.")
            delete_char.reset_cooldown(ctx) # repl.it just drunk, It works, Don't mind it
            return
        
        if m.content != ctx.author.nick:
            await mess.edit(content="Canceled.")
            return

        ret = await delete_profile(ctx.author.id)

        if ret["ret"]:
            await ctx.send("Successfully delete your profile!")
            await self.bot.update_role(ctx)
        else:
            await ctx.send(":x: **Unable to delete your profile, Please try again later!**")


def setup(bot: Bot) -> None:
    bot.add_cog(CrusaderProfile(bot))