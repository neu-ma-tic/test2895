from discord import Embed
from discord.ext.commands import command
from core.classes import Cog_Extension
from cmds.jfile import open_jfile
from const import units, response
from random import choice, uniform
import datetime

jdata = open_jfile('settings.json')

pic_link = jdata['pic_link']

class Fun(Cog_Extension):

    @command(aliases = ['Say', 's', 'S'])
    async def say(self, ctx, *, msg = None):
        if ctx.message.author.id == 418428531572342794:
            await ctx.message.delete()
            if msg != None:
                await ctx.send(msg)

    @command()
    async def 我是誰(self, ctx):
        if ctx.message.author.id == 418428531572342794:
            message = '我親愛的主人！(๑ơ ₃ ơ)♥'
        else:
            message = '哼！別想騙我了。除了主人以外的人都是骯髒變態！'
        embed = Embed(title = message, color = 0xff004b)
        await ctx.send(embed = embed)

    @command(aliases = ['WhoAmI'])
    async def whoami(self, ctx):
        if ctx.message.author.id == 418428531572342794:
            message = 'You are my master! (๑ơ ₃ ơ)♥'
        else:
            message = 'Pervert!'
        embed = Embed(title = message, color = 0xff004b)
        await ctx.send(embed = embed)

    @command()
    async def 長度(self, ctx, tag = None):
        length = str(round(uniform(0.0, 20.0), 2)) + ' ' + choice(units)
        if tag != None:
            if tag[:3] == '<@!' and tag[len(tag) - 1] == '>':
                s = tag + ' 就長這麼短，只有'
        else:
            s = '你就長這麼短， 只有'
        embed = Embed(title = '長度', color = 0xff004b, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = '\u200b', value = s + length + '。')
        embed.set_image(url = pic_link[0])
        if tag != None:
            if tag == '<@!418428531572342794>':
                embed = Embed(title = '不要弄玩我家主人好嗎？你這臭蟲。', color = 0xff004b)
            elif tag == f'<@!{str(self.bot.user.id)}>':
                embed = Embed(title = '很好玩嗎？垃圾。', color = 0xff004b)
        await ctx.send(embed = embed)

    @command()
    async def 精子濃度(self, ctx, tag = None):
        concentration = str(round(uniform(0.0, 7.0), 2)) + '%'
        if tag != None:
            if tag[:3] == '<@!' and tag[len(tag) - 1] == '>':
                s = '， ' + tag + ' 的家明就只有這麼稀'
        else:
            s = '， 你的家明就只有這麼稀'
        embed = Embed(title = '精子濃度', color = 0xff004b, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = '\u200b', value = concentration + s + '。')
        embed.set_image(url = pic_link[0])
        if tag != None:
            if tag == '<@!418428531572342794>':
                embed = Embed(title = '不要弄玩我家主人好嗎？你這臭蟲。', color = 0xff004b)
            elif tag == f'<@!{str(self.bot.user.id)}>':
                embed = Embed(title = '很好玩嗎？垃圾。', color = 0xff004b)
        await ctx.send(embed = embed)

    @command()
    async def 八號球(self, ctx, questions = None):
        if ctx.message.author.id == 418428531572342794:
            if questions == None:
                embed = Embed(title = '愛您喔主人！(≧▽≦)', color = 0xff004b)
            else:
                embed = Embed(title = '是的，主人。', color = 0xff004b)
            embed.set_image(url = pic_link[6])
        else:
            embed = Embed(title = choice(response), color = 0xff004b)
            if embed.title == '愛您喔！(>ω<)':
                embed.set_image(url = pic_link[len(pic_link) - 2])
            elif embed.title == '才不是啊！你這大蠢材！':
                embed.set_image(url = pic_link[3])
            elif embed.title == '欸……這人沒救了……':
                embed.set_image(url = pic_link[5])
            elif embed.title == '你這變態！' or 'Kono Hentai！' or 'この変態！':
                embed.set_image(url = pic_link[4])
            elif embed.title == 'Baka！Aho！' or 'バカ！アホ！' or 'Kono Baka！～(>.<)' or 'このばか！～(>.<)':
                embed.set_image(url = pic_link[2])
            elif embed.title == '最討厭你了！':
                embed.set_image(url = pic_link[7])
            elif embed.title == '才…才不是喜歡呢你哼！':
                embed.set_image(url = pic_link[8])
            elif embed.title == '⠀':
                embed.set_image(url = pic_link[9])
            else:
                embed.set_image(url = pic_link[1])
        await ctx.send(embed = embed)

    @command(aliases = ['EightBall', '8ball', '8Ball'])
    async def eightball(self, ctx, questions = None):
        if ctx.message.author.id == 418428531572342794:
            if questions == None:
                embed = Embed(title = 'Love you, my master! (≧▽≦)', color = 0xff004b)
            else:
                embed = Embed(title = 'Yes, my master.', color = 0xff004b)
        else:
            b = choice(['Yes', 'No'])
            embed = Embed(title = b, color = 0xff004b)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Fun(bot))