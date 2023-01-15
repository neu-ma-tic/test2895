#Credit VACEfron.py (module vacefron) to VAC Efron & Soheab
#https://github.com/Soheab/vacefron.py

#Credit Disputils (module disputils) to LiBa001, crazygmr101, lorddusk, AlphaMycelium and Skullbite
#https://github.com/LiBa001/disputils

#Credit avamember.avatar_url to Kelo
#https://stackoverflow.com/questions/59799987/how-to-get-a-users-avatar-with-their-id-in-discord-py

#Credit the method of sorting a dictionary by value to Dima Tisnek
#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

import json, asyncio
from discord import Member, File, Embed
from discord.ext.commands import command
from core.classes import Cog_Extension
from cmds.jfile import open_jfile
from datetime import datetime

try:
    from vacefron import Client
except ImportError:
    from os import system
    system('python -m pip install -U git+https://github.com/Soheab/vacefron.py')
    from vacefron import Client

try:
    from disputils import BotEmbedPaginator
except ImportError:
    from os import system
    system('python -m pip install disputils -U')
    from disputils import BotEmbedPaginator

vac_api = Client()

class Ranking_System(Cog_Extension):

    @command(aliases = ['Rank', 'r', 'R'])
    async def rank(self, ctx, avamember : Member = None):

        def __init__(self, * args, ** kwargs):

            super().__init__(* args, ** kwargs)

            async def interval():

                def monthly_top():
                    ranks = open_jfile('ranks.json')
                    l = {}
                    for user_id in ranks.keys():
                        username = self.bot.get_user(int(user_id))
                        l.update({username : [user_id, ranks[user_id]['rank']]})
                    l = {k : v for k, v in sorted(l.items(), key = lambda item : item[1][1])}
                    embed = Embed(title = 'Top:', description = 'Global Rank', color = 0xff004b, timestamp = datetime.utcnow())
                    #await self.top_channel.send(embed = embed)
                    #await asyncio.sleep(2635200)  #int(60 * 60 * 24 * 30.5) == 2635200 (1 month)

                await self.bot.wait_until_ready()
                while not self.bot.is_closed():
                    monthly_top(self)

            self.bg_task = self.bot.loop.create_task(interval())

        def next_level_xp(level):
            if level >= 500:
                xp = 0
            else:
                xp = round((1000 + 1.125 ** (level / 12.5) - 1 - 1.28 ** (level / 100) * level / 1000) * 1000)
            return xp

        def previous_level_xp(level):
            if level == 0:
                xp = 0
            else:
                xp = round((1000 + 1.125 ** ((level - 1) / 12.5) - 1 - 1.28 ** ((level - 1) / 100) * (level - 1) / 1000) * 1000)
            return xp

        ranks = open_jfile('ranks.json')
        if avamember == None:
            info = ranks[f'{ctx.author.id}']
            username = ctx.author.name
            avatar = ctx.author.avatar_url
            boosting = True if ctx.author.premium_since else False
        else:
            info = ranks[str(avamember.id)]
            username = avamember
            avatar = avamember.avatar_url
            boosting = True if avamember.premium_since else False
        card_pic = None
        if int(info['rank']) == -1:
            color = '861D9E'
            card_pic = 'https://i.imgur.com/J4ycHw7.png'
        elif int(info['rank']) == 0:
            color = 'FF004B'
            card_pic = 'https://i.imgur.com/hRnlFfy.png'
        else:
            color = 'FCBA41'
        gen_card = await vac_api.rank_card(
            username = username,
            avatar = avatar,
            level = int(info['level']),
            rank = int(info['rank']),
            current_xp = int(info['current_xp']),
            next_level_xp = next_level_xp(int(info['level'])),
            previous_level_xp = previous_level_xp(int(info['level'])),
            custom_background = card_pic,
            xp_color = color,
            is_boosting = boosting
            )
        rank_bytes = await gen_card.read()
        #await ctx.send(f"{username}'s rank in {ctx.guild.name}",
                      #file = discord.File(rank_bytes, f'{username}_rank.png')
                      #)
        await ctx.send(f"{username}'s global rank",
                      file = File(rank_bytes, f'{username}_rank.png')
                      )

    @command(aliases = ['Levels', 'l', 'L'])
    async def levels(self, ctx):
        ranks = open_jfile('ranks.json')
        l = {}
        for user_id in ranks.keys():
            username = self.bot.get_user(int(user_id))
            l.update({username : [user_id, ranks[user_id]['rank']]})
        l = {k : v for k, v in sorted(l.items(), key = lambda item : item[1][1])}
        embed = Embed(title = 'Top:', description = 'Global Rank', color = 0xff004b, timestamp = datetime.utcnow())
        embed_list = []
        n = 0
        for username in l.keys():
            if l[username][1] < 1:
                inline = False
            else:
                inline = True
            embed.add_field(name = f'Rank #{l[username][1]}', value = f"{username} (Lv {ranks[l[username][0]]['level']})", inline = inline)
            n += 1
            if n % 25 == 0 or n == len(l):
                embed_list.append(embed)
                if n != len(l):
                    embed = Embed(title = 'Top:', description = 'Global Rank', color = 0xff004b, timestamp = datetime.utcnow())
        paginator = BotEmbedPaginator(ctx, embed_list)
        await paginator.run()

    @command(aliases = ['SetRankChannel', 'src', 'SRC'])
    async def setrankchannel(self, ctx, ch : int):
        self.rank_channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Rank Channel: {self.rank_channel.mention}')

    @command(aliases = ['SetTopChannel', 'stc', 'STC'])
    async def settopchannel(self, ctx, ch : int):
        self.top_channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Top Channel: {self.top_channel.mention}')

def setup(bot):
    bot.add_cog(Ranking_System(bot))