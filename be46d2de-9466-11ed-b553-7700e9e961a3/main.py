import os
import logging

from utils.log import setup
from bot import Bot

from webserver import keep_alive

# Keep repl.it running.
# Need to be use with UptimeRobot.
keep_alive()

# Setting up Logging.
setup()
log = logging.getLogger("main")
log.info("Starting program...")

# Create and Run the Bot.
bot = Bot.create()
bot.load_extensions()

token = os.getenv("token")
bot.run(token)