from discord import Member, Embed
from discord.ext.commands import command
from core.classes import Cog_Extension
from cmds.jfile import open_jfile
from const import welcome_message
import datetime

jdata = open_jfile('settings.json')

pic_link = jdata['pic_link']

class Joining(Cog_Extension):

    @command(aliases = ['Welcome', 'w', 'W'])
    async def welcome(self, ctx, avamember : Member = None):
        v = 'Newcomer'
        if avamember != None:
            v = f'<@!{avamember.id}>'
        embed = Embed(title = welcome_message, color = 0xff004b, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = 'Welcome!', value = v, inline = True)
        embed.set_image(url = pic_link[len(pic_link) - 5])
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Joining(bot))