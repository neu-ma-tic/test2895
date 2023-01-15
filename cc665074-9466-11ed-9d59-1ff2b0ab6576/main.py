#L_Maid(Discord_Bot).py

#Lilin莉莉（路姐的傲嬌女僕 (Discord Bot)
#Created on 5/7/2020 by Lucifer

from discord.ext.commands import Bot
from discord import Game, Status
from keep_alive import keep_alive
from cmds.jfile import open_jfile
from os import system, listdir
from sqlite3 import connect
from datetime import datetime

system('/opt/virtualenvs/python3/bin/python -m pip install --upgrade pip')
system('/opt/virtualenvs/python3/bin/python -m pip install discord -U')

bot = Bot(command_prefix = 'm!', description = '')

jdata = open_jfile('settings.json')

TOKEN = jdata['TOKEN']

bot.remove_command('help')

for filename in listdir('./cmds'):
    if filename.endswith('.py') and filename != 'jfile.py':
        bot.load_extension(f'cmds.{filename[:-3]}')

conn = connect('player.db')

cursor = conn.execute('''
SELECT * FROM PLAYERWEAPON;
''')

@bot.event
async def on_ready():
    print(f'Bot is alive.\n{bot.guilds}')
    await bot.change_presence(status = Status.online, activity = Game(name = 'm!help | https://discord.com/api/oauth2/authorize?client_id=729380731289075773&permissions=2147483647&scope=bot', start = datetime(30, 1, 1)), afk = False)
    banned_guild = bot.get_guild(688327700083114011) #744540580419338252
    print(banned_guild.name)
    for i in banned_guild.members:
        print(i)

if __name__ == '__main__':

    keep_alive()
    bot.run(TOKEN)