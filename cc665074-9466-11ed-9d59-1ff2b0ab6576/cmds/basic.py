from discord import Embed, __version__
from discord.ext.commands import command
from core.classes import Cog_Extension
from cmds.jfile import open_jfile
from socket import gethostbyname, gethostname

jdata = open_jfile('settings.json')

pic_link = jdata['pic_link']

class Basic(Cog_Extension):

    @command(aliases = ['Ip_address', 'ip', 'IP'])
    async def ip_address(self, ctx):
        if ctx.author.id == 418428531572342794:
            embed = Embed(title = 'Bot Local IP Address', description = f'`{gethostbyname(gethostname())}`', color = 0xff004b)
            await ctx.send(embed = embed)

    @command(aliases = ['Profile', 'p', 'P'])
    async def profile(self, ctx):
        embed = Embed(title = 'Profile', color = 0xff004b)
        embed.set_author(name ='Lilin', icon_url = pic_link[len(pic_link) - 3])
        embed.set_thumbnail(url = pic_link[len(pic_link) - 4])
        embed.add_field(name ='Self-Introduction:', value = '予乃莉莉，夜之魔女莉莉絲之息女，\n魔族中最出色的戰鬥女僕。\n永遠跟隨最強的傲慢魔王路西法。\n所有下賤的人類都是蛆蟲！\n欲碰主人一根頭髮的臭蟲們，先過予這關！\n喜歡的顏色：紅黑色\n世上最美的人：路西法\n和主人一樣，討厭人類和變態。', inline = False)
        embed.add_field(name ='Name:', value = 'Lilin', inline = False)
        embed.add_field(name ='Species:', value = '小悪魔(Imp)')
        embed.add_field(name ='Sex:', value = '女性(Female)')
        embed.add_field(name ='Age:', value = '450yrs')
        embed.add_field(name ='Irises Colours:', value = 'Left -Yellow\nRight -Red', inline = False)
        embed.add_field(name ='Master:', value = 'Lucifer <@!418428531572342794>', inline = False)
        embed.add_field(name ='Role:', value = 'Maid', inline = False)
        embed.add_field(name ='Parents:', value = 'Mother -リリス(Lilith)\nFather -アダム(Adam)', inline = False)
        embed.add_field(name ='Battle Power:', value = '350,000')
        embed.add_field(name ='Commonly Used Weapon:', value = 'トライデント(Trident)')
        embed.add_field(name ='Ultimate Skill:', value = '漆黒の迅撃')
        await ctx.send(embed = embed)

    @command(aliases = ['Informations', 'info', 'Info'])
    async def informations(self, ctx):
        embed = Embed(title = 'Informations', description = "This bot is my maid. She's definitely a tsundere.", color = 0xff004b)
        embed.set_author(name ='Lucifer', icon_url = pic_link[len(pic_link) - 1])
        embed.set_thumbnail(url = pic_link[len(pic_link) - 3])
        embed.add_field(name ='Prefix', value = 'm!', inline = False)
        embed.add_field(name ='Username', value = self.bot.user.name, inline = False)
        embed.add_field(name ='Bot ID', value = self.bot.user.id, inline = True)
        embed.add_field(name ='Author', value = '<@!418428531572342794>', inline = True)
        embed.add_field(name ='Server count', value = f'{len(self.bot.guilds)}', inline = True)
        embed.add_field(name ='Library', value = 'discord.py ' + __version__, inline = False)
        embed.add_field(name ='Invite', value = 'https://discord.com/api/oauth2/authorize?client_id=729380731289075773&permissions=2147483647&scope=bot', inline = False)
        await ctx.send(embed = embed)

    @command()
    async def ping(self, ctx):
        embed = Embed(title = 'Ping', color = 0xff004b)
        embed.add_field(name ='Ping in miniseconds:', value = f'{round(self.bot.latency * 1000)}ms')
        await ctx.send(embed = embed)

    @command(aliases = ['Help', 'h', 'H'])
    async def help(self, ctx):

        embed = Embed(title = 'Help', description = 'List of commands are:', color = 0xff004b)

        embed.add_field(name = 'm!welcome/m!Welcome/m!w/m!W', value = 'Manually sends the welcome message.', inline = False)

        embed.add_field(name = 'Moderation (for admin use only)', value = 'Commands:', inline = False)
        embed.add_field(name = 'm!purge/m!Purge/m!pu/m!Pu', value = 'Delete a certain amount of messages in the current channel.', inline = True)
        embed.add_field(name = 'm!purgeall/m!PurgeAll/m!pa/m!PA', value = 'Delete all messages in the current channel.', inline = True)
        embed.add_field(name = 'm!giverole', value = 'Give a existing role to a member.\n(Special role "Rank SSSS+ Demon Lord" is required.)', inline = True)
        embed.add_field(name = 'm!removerole', value = 'Remove one role from a member.\n(Special role "Rank SSSS+ Demon Lord" is required.)', inline = True)

        embed.add_field(name = 'm!rank/m!Rank/m!r/m!R', value = "Check your/other's current level, current xp, xp required for upgrading to next level and global rank.", inline = False)

        embed.add_field(name = 'Fun', value = 'Commands:', inline = False)
        embed.add_field(name = 'm!我是誰', value = 'Check whether you are the master of this maid.\n(in Chinese)', inline = True)
        embed.add_field(name = 'm!whoami/m!WhoAmI', value = 'Check whether you are the master of this maid\n(in English).', inline = True)
        embed.add_field(name = 'm!長度', value = "Checks the length of your/others' dick.", inline = True)
        embed.add_field(name = 'm!精子濃度', value = "Checks your/other's sperm concentration.", inline = True)
        embed.add_field(name = 'm!八號球', value = 'Answers your questions.\n(in Chinese)', inline = True)
        embed.add_field(name = 'm!eightball/m!EightBall/m!8ball/m!8Ball', value = 'Answers your questions.\n(in English)', inline = True)

        embed.add_field(name = 'Basic', value = 'Commands:', inline = False)
        embed.add_field(name = 'm!profile/m!Profile/m!p/m!P', value = 'Gives the profile, and anything about this maid', inline = True)
        embed.add_field(name = 'm!informations/m!Informations/m!info/m!Info', value = 'Gives the informin ations of this bot', inline = True)
        embed.add_field(name = 'm!help/m!Help/m!h/m!H', value = 'Gives this message', inline = True)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Basic(bot))