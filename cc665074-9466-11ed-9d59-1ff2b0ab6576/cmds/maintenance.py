from discord.ext.commands import command
from core.classes import Cog_Extension

class Maintenance(Cog_Extension):

    @command()
    async def load(self, ctx, extension):
        if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 418428531572342794:
            self.bot.load_extension(f'cmds.{extension}')
            await ctx.send(f'{extension} is loaded.')
        else:
            await ctx.send('Permission denied.')

    @command()
    async def unload(self, ctx, extension):
        if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 418428531572342794:
            self.bot.unload_extension(f'cmds.{extension}')
            await ctx.send(f'{extension} is unloaded.')
        else:
            await ctx.send('Permission denied.')

    @command()
    async def reload(self, ctx, extension):
        if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 418428531572342794:
            self.bot.reload_extension(f'cmds.{extension}')
            await ctx.send(f'{extension} is reloaded.')
        else:
            await ctx.send('Permission denied.')

def setup(bot):
    bot.add_cog(Maintenance(bot))