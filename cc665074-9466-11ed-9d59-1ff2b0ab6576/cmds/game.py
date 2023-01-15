#Credit get a list of column names in sqlite to isedwards&smallredstone
#https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite

from sqlite3 import connect
from discord import Member, Embed
from discord.ext.commands import command
from core.classes import Cog_Extension
from cmds.jfile import open_jfile
from datetime import datetime

jdata = open_jfile('settings.json')

weapons = jdata['weapons']

common = weapons['common']
uncommon = weapons['uncommon']
rare = weapons['rare']
super_rare = weapons['super rare']
ultra_rare = weapons['ultra rare']

shop_items = jdata['shop items']

class Game(Cog_Extension):

    @command()
    async def start(self, ctx, player_type = None):

        def check_exist(id):
            conn = connect('player.db')
            cursor = conn.execute('''
            SELECT ID FROM PLAYER;
            ''')
            exist = False
            for i in cursor:
                if id == i:
                    exist = True
                    break
            conn.close()
            return exist

        def register(id, name, player_type, level):
            conn = connect('player.db')
            sql = f'''
            INSERT INTO PLAYER
            (
              ID, PLAYERNAME, TYPE, LEVEL, ENERGON, GOLD
            )
            VALUES
            (
              {id}, '{name}', '{player_type}', {level}, 100, 500
            );
            '''
            conn.execute(sql)
            conn.commit()
            conn.close()

        id = ctx.message.author.id
        ranks = open_jfile('ranks.json')
        level = ranks[f'{id}']['level']
        exist = check_exist(id)
        if exist:
            await ctx.send('**Player has already registered.**')
        elif player_type != None:
            player_type = str(player_type)
            if player_type == 'Attacker' or player_type == 'Defender' or player_type == 'Magician':
                user = self.bot.get_user(id)
                register(id, user.name, player_type, level)
                await ctx.send('**New player has been succcessfully registered as follow:**')
                embed = Embed(title = 'Player Profile', color = 0xff004b, timestamp = datetime.utcnow())
                embed.add_field(name = 'Player name:', value = user.name, inline = True)
                embed.add_field(name = 'Player type:', value = player_type, inline = True)
                embed.add_field(name = 'Player level:', value = level, inline = True)
                embed.add_field(name = 'Energon:', value = 100, inline = True)
                embed.add_field(name = 'Gold:', value = 500, inline = True)
                await ctx.send(embed = embed)
            else:
                await ctx.send('**Invalid player type. (Attacker/Defender/Magician)**')
        else:
            await ctx.send('**Player type is missing. (Attacker/Defender/Magician)**')

    @command()
    async def player(self, ctx,  avamember : Member = None):
        id = ctx.message.author.id
        conn = connect('player.db')
        sql = f'''
        SELECT *
        FROM PLAYER
        WHERE ID = {id}
        '''
        cursor = conn.execute(sql)
        embed = Embed(title = 'Player Profile', color = 0xff004b, timestamp = datetime.utcnow())
        names = list(map(lambda x: x[0], cursor.description))
        rows = cursor.fetchall()
        row = rows[0]
        for n in range(len(names)):
            embed.add_field(name = names[n], value = row[n], inline = False)
        embed.add_field(name = 'List Of Weapons:', value = '⠀', inline = False)
        sql = f'''
        SELECT WEAPONNAME, WEAPONLEVEL
        FROM PLAYERWEAPON
        WHERE PLAYERID = {id}
        '''
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        print(rows)
        for n in range(len(rows)):
            embed.add_field(name = rows[n][0], value = 'Level: ' + str(rows[n][1]), inline = False)
        conn.close()
        await ctx.send(embed = embed)

    @command()
    async def shop(self, ctx):
        id = ctx.message.author.id
        conn = connect('player.db')
        cursor = conn.execute(f'''
        SELECT GOLD FROM PLAYER WHERE ID = {id};
        ''')
        for g in cursor:
            gold = g
        conn.close()
        embed = Embed(title = 'Shop', color = 0xff004b, timestamp = datetime.utcnow())
        embed.add_field(name = 'Commands:', value = 'm!buy [Item ID]', inline = False)
        embed.add_field(name = 'Beginner weapon:', value = '200G', inline = False)
        embed.add_field(name = common['c001'][0] + ' (c001)', value = common['c001'][1] + ' (+10ATK)', inline = True)
        embed.add_field(name = common['c002'][0] + ' (c002)', value = common['c002'][1] + ' (+10DEF)', inline = True)
        embed.add_field(name = common['c003'][0] + ' (c003)', value = common['c003'][1] + ' (+5MATK +5MDEF)', inline = True)
        embed.add_field(name = 'Credits', value = gold, inline = False)
        await ctx.send(embed = embed)

    @command()
    async def buy(self, ctx, item_id = None):
        if item_id == None:
            await ctx.send('**Item ID is missing.**')
        elif item_id in shop_items:
            id = ctx.message.author.id
            conn = connect('player.db')
            cursor = conn.execute(f'''
            SELECT GOLD FROM PLAYER WHERE ID = {id};
            ''')
            for g in cursor:
                gold = g
            if gold != None:
                gold = gold[0]
                if gold > 0 or id == 418428531572342794:
                    remaining_gold = gold - shop_items[item_id]
                    if remaining_gold >= 0 or id == 418428531572342794:
                        if id == 418428531572342794:
                            sql = f'''
                            UPDATE PLAYER
                            SET GOLD = {remaining_gold}
                            WHERE ID = {id};
                            '''
                            conn.execute(sql)
                            conn.commit()
                            conn.close()
                        for key_1 in weapons:
                            for key_2 in weapons[key_1]:
                                if key_2 == item_id:
                                    weapon_name = weapons[key_1][key_2][0]
                                    weapon_type = weapons[key_1][key_2][1]
                                    rarity = key_1
                                    break
                        conn = connect('player.db')
                        sql ='''SELECT COUNT(*) FROM PLAYERWEAPON
                        '''
                        cursor = conn.execute(sql)
                        cursor = conn.cursor()
                        row = cursor.fetchone()
                        if row != None:
                            data_id = len(row) + 1
                        else:
                            data_id = 1
                        sql = f'''
                        INSERT INTO PLAYERWEAPON
                        (
                          ID, WEAPONID, WEAPONNAME, WEAPONTYPE, WEAPONLEVEL, PLAYERID
                        )
                        VALUES
                        (
                          {data_id}, '{item_id}', '{weapon_name}', '{weapon_type}', 1, {id}
                        );
                        '''
                        conn.execute(sql)
                        conn.commit()
                        conn.close()
                        item_name = weapons[rarity][item_id][0]
                        item_type = weapons[rarity][item_id][1]
                        item_pic_url = weapons[rarity][item_id][2]
                        embed = Embed(title = 'Receipt', color = 0xff004b, timestamp = datetime.utcnow())
                        embed.set_thumbnail(url = item_pic_url)
                        embed.add_field(name = 'Item ID:', value = item_id, inline = False)
                        embed.add_field(name = 'Item Name:', value = item_name, inline = False)
                        embed.add_field(name = 'Item Type:', value = item_type, inline = False)
                        embed.add_field(name = 'Price:', value = shop_items[item_id], inline = False)
                        embed.add_field(name = 'Gold Before Purchase:', value = gold, inline = False)
                        embed.add_field(name = 'Gold After Purchase:', value = remaining_gold, inline = False)
                        await ctx.send(embed = embed)
                    else:
                        await ctx.send('**Not enough gold.**')
                else:
                    await ctx.send("**Poor you. You don't have any gold.**")
        else:
            await ctx.send('**Invalid item ID is missing.**')

def setup(bot):
    bot.add_cog(Game(bot))