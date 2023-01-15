import os
from discord_easy_commands import EasyBot
bot = EasyBot()
bot.run(os.environ['TOKEN'])