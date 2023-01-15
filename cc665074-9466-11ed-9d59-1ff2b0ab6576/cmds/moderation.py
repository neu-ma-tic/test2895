#Credit the function giverole to Mr Fuzzy
#https://stackoverflow.com/questions/49076798/discord-py-add-role-to-someone

from discord import User, Member, Role, Embed
from discord.ext.commands import command, has_permissions
from core.classes import Cog_Extension
from cmds.jfile import open_jfile
import datetime

jdata = open_jfile('settings.json')

server_id = jdata['server id']

def check_role(ctx):
    def get_supreme_role(id):
        supreme_role = server_id[f'{id}']['supreme role']
        return supreme_role
    supreme_role = get_supreme_role(ctx.message.guild.id)
    if supreme_role in [y.name for y in ctx.message.author.roles]:
        return True
    else:
        return False

class Moderation(Cog_Extension):

    @command(pass_context = True)
    @has_permissions(administrator = True)
    async def kick(self, ctx, * userNames : User):
        for userName in userNames:
            await ctx.guild.kick(userName)
            await ctx.send("Member(s) kicked.")

    @command(pass_context = True)
    async def chnick(self, ctx, member : Member = None, nick = None):
        if member != None:
            if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 418428531572342794:
                await ctx.send(f'Nickname was changed for {member.mention} .')
            else:
                await ctx.send('Permission denied.')
        else:
            member = ctx.message.server.get_member(ctx.message.author.id)
            await ctx.send(f'Your was changed to .')
        await ctx.message.delete()
        await member.edit(nick = nick)

    @command(aliases = ['Purge', 'pu', 'Pu'])
    @has_permissions(administrator = True)
    async def purge(self, ctx, num : int):
        await ctx.channel.purge(limit = num + 1)

    @command(aliases = ['PurgeAll', 'pa', 'PA'])
    @has_permissions(administrator = True)
    async def purgeall(self, ctx):
        await ctx.channel.purge()

    @command(pass_context = True)
    @has_permissions(administrator = True)
    async def giverole(self, ctx, user : Member, role : Role):
        if check_role(ctx):
            await user.add_roles(role)
            embed = Embed(title = 'Promotion', color = 0xff004b, timestamp = datetime.datetime.utcnow())
            embed.add_field(name = '⠀', value = f'Congratulations! {user.mention}\nYou has been giving a role called: <@&{role.id}>\n    {user.name} should give thanks to {ctx.author.name}')
            await ctx.send(embed = embed)
        else:
            await ctx.send('Permission denied.')

    @command(pass_context = True)
    @has_permissions(administrator = True)
    async def removerole(self, ctx, user : Member, role : Role):
        if check_role(ctx):
            await user.remove_roles(role)
            embed = Embed(title = 'Demotion', color = 0xff004b, timestamp = datetime.datetime.utcnow())
            embed.add_field(name = '⠀', value = f'{user.mention}\nYour role {role.name} has been removed!\nThis is the order from {ctx.author.name}')
            await ctx.send(embed = embed)
        else:
            await ctx.send('Permission denied.')

def setup(bot):
    bot.add_cog(Moderation(bot))