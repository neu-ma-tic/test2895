import logging

logging.basicConfig(level=logging.DEBUG)

for pkg_ in ["discord", "asyncio"]:
    logging.getLogger(pkg_).setLevel(logging.ERROR)

logger = logging.getLogger(__package__)
