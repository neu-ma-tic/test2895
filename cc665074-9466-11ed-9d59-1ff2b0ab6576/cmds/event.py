from discord import Embed
from discord.ext import commands
from discord.ext.commands import Cog
from core.classes import Cog_Extension
from cmds.jfile import open_jfile, write_json
from const import welcome_message
from datetime import datetime
from random import choice

jdata = open_jfile('settings.json')

server_id = jdata['server id']
pic_link = jdata['pic_link']
banned_guild_ids = [
  #688327700083114011
  ]

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            welcome_channel = self.bot.get_channel(server_id[f'{member.guild.id}']['welcome channel id'])
        except:
            welcome_channel = choice(member.guild.text_channels)
        embed = Embed(title = welcome_message, color = 0xff004b, timestamp = datetime.utcnow())
        tag = '<@!' + str(member.id) + '>'
        embed.add_field(name = 'Welcome!', value = tag, inline = True)
        embed.add_field(name = '<:103886497_2945835718804584_67551:728368418209792020> <:108006755_3118478104907540_82111:733523276730728460>', value = '⠀', inline = True)
        try:
            if server_id[f'{member.guild.id}']['rules channel id'] != None:
                id = server_id[f'{member.guild.id}']['rules channel id']
                embed.add_field(name = 'For all newcomers,', value = f'go to <#{id}> and read the rules now.', inline = False)
        except:
            pass
        embed.set_image(url = pic_link[len(pic_link) - 5])
        await welcome_channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        try:
            leave_channel = self.bot.get_channel(server_id[f'{member.guild.id}']['welcome channel id'])
        except:
            leave_channel = choice(member.guild.text_channels)
        if member.id == 418428531572342794:
            embed = Embed(title = f'高貴的 {member} 主人為甚麼離開我！\n不！(இ﹏இ`｡)', color = 0xff004b, timestamp = datetime.utcnow())
        else:
            embed = Embed(title = f'Oh No! {member} has left us. >_<', color = 0xff004b, timestamp = datetime.utcnow())
        embed.add_field(name = '<:103663021_260413651949867_658972:722754276857741332>', value = '⠀')
        embed.set_image(url = pic_link[len(pic_link) - 6])
        await leave_channel.send(embed = embed)
        if member.id == 418428531572342794:
            embed = Embed(title = f'Now we salute to our fellow demon lord, {member}.', color = 0xff004b, timestamp = datetime.utcnow())
            embed.add_field(name = 'Please rise,', value = '@everyone')
            embed.set_image(url = pic_link[len(pic_link) - 7])
            await leave_channel.send(embed = embed)
            await leave_channel.send('https://www.youtube.com/watch?v=UCCyoocDxBA')

    @Cog.listener()
    async def on_message(self, msg):

        def gain_xp(id):

            def existing_profile(id, ranks):

                def get_current_rank(id, ranks):

                    def total_xp(lv, current):
                        total = current
                        while lv != 0:
                            previous_level_xp = round((1000 + 1.125 ** ((lv - 1) / 12.5) - 1 - 1.28 ** ((lv - 1) / 100) * (lv - 1) / 1000) * 1000)
                            total += previous_level_xp
                            lv -= 1
                        return total

                    r = {}
                    for i in ranks.keys():
                        total = total_xp(ranks[i]['level'], ranks[i]['current_xp'])
                        r.update({f'{i}' : total})
                    r = {key : rank for rank, key in enumerate(sorted(r, key = r.get, reverse = True), 1)}
                    return r[id]

                rank_up = False
                level = ranks[id]['level']
                if level < 500:
                    ranks[id]['current_xp'] += 1000
                    next_level_xp = round((1000 + 1.125 ** (level / 12.5) - 1 - 1.28 ** (level / 100) * level / 1000) * 1000)
                    if ranks[id]['current_xp'] >= next_level_xp:
                        ranks[id]['current_xp'] -= next_level_xp
                        ranks[id]['level'] += 1
                        rank_up = True
                    for i in ranks.keys():
                        ranks[i]['rank'] = get_current_rank(i, ranks) - 2
                return ranks, rank_up

            def new_profile(ranks):
                y = {
                  "level" : 0,
                  "rank" : len(ranks) - 1,
                  "current_xp" : 5000
                  }
                x = {f'{id}' : y}
                ranks.update(x)
                return ranks

            ranks = open_jfile('ranks.json')
            id = str(id)
            rank_up = False
            if id in ranks:
              ranks, rank_up = existing_profile(id, ranks)
            else:
                ranks = new_profile(ranks)
            write_json(ranks, 'ranks.json', 3)
            return rank_up, ranks[id]['level']

        jdata = open_jfile('settings.json')
        梗圖 = jdata['梗圖']
        tag = None
        last = msg.content.split(' ')[len(msg.content.split(' ')) - 1]
        if last[0] == '@' or last[:2] == '<@' and last[len(last) - 1] == '>':
            tag = msg.content.split(' ')[len(msg.content.split(' ')) - 1]
        content = msg.content
        if tag != None:
            content = msg.content.replace(f' {tag}', '', 1)
        if msg.content.lower() == f'<@!{str(self.bot.user.id)}> hi':
            await msg.channel.send(f'Привет, {msg.author.mention}')
        elif msg.content.lower().endswith(f'<@!{str(self.bot.user.id)}>'):
            await msg.channel.send('Круто')
        elif content.lower() in 梗圖.keys():
            embed = Embed(title = 'Image', url = 梗圖[content.lower()], color = 0xff004b, timestamp = datetime.utcnow())
            if tag == None:
                tag = '\u200b'
            embed.add_field(name = content, value = tag)
            embed.set_image(url = 梗圖[content.lower()])
            await msg.channel.send(embed = embed)
        if not msg.author.bot:
            rank_up, level = gain_xp(msg.author.id)
            if rank_up:
                if server_id[f'{msg.guild.id}']['rank check channel id'] != None:
                    channel = self.bot.get_channel(server_id[f'{msg.guild.id}']['rank check channel id'])
                    await channel.send(f'Congragulations  {msg.author.mention}! You just advanced to level {level}!')
                else:
                    await msg.channel.send(f'Congragulations  {msg.author.mention}! You just advanced to level {level}!')

def setup(bot):
    bot.add_cog(Event(bot))