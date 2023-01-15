# discord.ext.commands.Bot custom Subclass 
# Made by Tpmonkey

import asyncio
import logging

import discord
from discord.ext import commands

from constant import Database
from utils.manager import add_cp, remove_cp, add_ocp, remove_ocp, get_data, check
from utils.roles_id import (
    _crusader_,  _officer_ , ocp_lv_to_id, cp_lv_to_id
)

log = logging.getLogger(__name__)
OWNERS = [574704384462815252, 518063131096907813]


class Bot(commands.Bot):
    # Subclass of commands.Bot
    def __init__(self, command_prefix, help_command=None, description=None, **options):
        # Set default Help command
        if not help_command:
            help_command = commands.DefaultHelpCommand()

        super().__init__(command_prefix, help_command, description, **options)

        # Define database here so It's easier to be use.
        self.database = Database()
        log.info("Bot Subclass Created.")

    @classmethod
    def create(cls) -> "Bot":
        # Create bot Instance and return

        loop = asyncio.get_event_loop()
        intents = discord.Intents().all()

        return cls(
            loop=loop,
            command_prefix="c!",
            # activity=discord.Game(name="with API and Mutiple Files."),
            # status=discord.Status.dnd,
            owner_ids = OWNERS,
            case_insensitive=False,
            max_messages=10_000,
            intents = intents
        )

    def load_extensions(self) -> None:
        # Load all extensions
        from utils.extensions import EXTENSIONS
        extensions = set(EXTENSIONS)

        for extension in extensions:
            self.load_extension(extension)

    def add_cog(self, cog: commands.Cog) -> None:
        # just for Logging
        super().add_cog(cog)
        log.info(f"Cog loaded: {cog.qualified_name}")
    
    async def wait_for_message(self, ctx: commands.Context, timeout: int = None) -> discord.Message:

        def check(m) -> bool:
            return m.channel == ctx.message.channel and m.author.id == ctx.author.id
        
        message = await self.wait_for("message", check=check, timeout=timeout)
        return message
    
    def get_role(self, ctx: commands.Context, role_id: int) -> discord.Role:
        return discord.utils.get(ctx.author.guild.roles, id=role_id)
    
    @staticmethod
    def to_number(number: int) -> str:
        return format(number, ",")
    
    async def add_role(self, ctx: commands.Context, role_id: int) -> None:
        role = self.get_role(ctx, role_id)
        try:
            await ctx.author.add_roles(role)
        except:
            return
        return
    
    async def remove_role(self, ctx: commands.Context, role_id: int) -> None:
        role = self.get_role(ctx, role_id)
        try:
            await ctx.author.remove_roles(role)
        except:
            return
        return
    
    async def _add_cp(self, ctx: commands.Context, target: discord.Member, amount: int = 1) -> discord.Embed:
        embed = discord.Embed(timestamp = ctx.message.created_at)

        ret = await add_cp(target.id, amount)

        if ret["success"]:
            embed.colour = discord.Colour.teal()
            embed.title = "Sucessfully!"
            embed.description = f"{target.nick} now has `{ret['cp']}` CP"
        else:
            embed.colour = discord.Colour.dark_red()
            embed.title = ":x: That user doesn't have an active profile!"

        return embed


    async def _remove_cp(self, ctx: commands.Context, target: discord.Member, amount: int = 1) -> discord.Embed:
        embed = discord.Embed(timestamp = ctx.message.created_at)

        ret = await remove_cp(target.id, amount)

        if ret["success"]:
            embed.colour = discord.Colour.teal()
            embed.title = "Sucessfully!"
            embed.description = f"{target.nick} now has `{ret['cp']}` CP"
        else:
            embed.colour = discord.Colour.dark_red()
            if ret["ret"] == "No Profile":                
                embed.title = ":x: That user doesn't have active profile!"
            else:
                embed.title = ":x: Cannot have negative value!"

        return embed
    
    async def _add_ocp(self, ctx: commands.Context, target: discord.Member, amount: int = 1) -> discord.Embed:
        embed = discord.Embed(timestamp = ctx.message.created_at)

        ret = await add_ocp(target.id, amount)

        if ret["success"]:
            embed.colour = discord.Colour.teal()
            embed.title = "Sucessfully!"
            embed.description = f"{target.nick} now has `{ret['ocp']}` OCP"
        else:
            embed.colour = discord.Colour.dark_red()
            if ret["ret"] == "Exceed Limit":
                embed.title = ":x: Exceed OCP Limit!"
            else:
                embed.title = ":x: That user doesn't have active profile!"

        return embed


    async def _remove_ocp(self, ctx: commands.Context, target: discord.Member, amount: int = 1) -> discord.Embed:
        embed = discord.Embed(timestamp = ctx.message.created_at)

        ret = await remove_ocp(target.id, amount)

        if ret["success"]:
            embed.colour = discord.Colour.teal()
            embed.title = "Sucessfully!"
            embed.description = f"{target.nick} now has `{ret['ocp']}` OCP"
        else:
            embed.colour = discord.Colour.dark_red()
            if ret["ret"] == "No Profile":                
                embed.title = ":x: That user doesn't have active profile!"
            else:
                embed.title = ":x: Cannot have negative value!"

        return embed
    
    async def update_role(self, ctx: commands.Context) -> None:
        roles = [role.id for role in ctx.author.roles]

        if not check(ctx.author.id):
            await self.remove_role(ctx, _crusader_)
            await self.remove_role(ctx, _officer_)

            all_roles = list()
            for key in cp_lv_to_id:
                all_roles.append(cp_lv_to_id[key])
            for key in ocp_lv_to_id:
                all_roles.append(ocp_lv_to_id[key])
            
            if any(role in roles for role in all_roles):
                for role in roles:
                    if role in all_roles:
                        await self.remove_role(ctx, role)
            return


        pp = get_data(ctx.author.id)["data"]
        lv = pp["cp-lv"]        

        if _crusader_ not in roles:
            await self.add_role(ctx, _crusader_)
        
        if lv != 0:        
            need_role = cp_lv_to_id[lv]
            if need_role not in roles:
                await self.add_role(ctx, need_role)
            
            dont_need_role = list()
            for i in cp_lv_to_id:
                if i == lv:
                    continue
                dont_need_role.append(cp_lv_to_id[i])

            for r in dont_need_role:
                if r in roles:
                    await self.remove_role(ctx, r)
        
        lv = pp["ocp-lv"]

        if lv != 0:
            if _officer_ not in roles:
                await self.add_role(ctx, _officer_)
            
            if lv != 0:        
                need_role = ocp_lv_to_id[lv]
                if need_role not in roles:
                    await self.add_role(ctx, need_role)
                
                dont_need_role = list()
                for i in ocp_lv_to_id:
                    if i == lv:
                        continue
                    dont_need_role.append(ocp_lv_to_id[i])

                for r in dont_need_role:
                    if r in roles:
                        await self.remove_role(ctx, r)