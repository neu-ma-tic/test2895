# Bot Backend
# Made by Tpmonkey
# Credit: Repl.it database

import logging
from typing import Any

from replit import db

LOG_CHANNEL = None # 782480899228434483

log = logging.getLogger(__name__)


class Database:
    async def check_connection(self) -> bool:
        # Check for connection
        try:
            w = db["waiting"]
        except:
            log.warn("Unable to connect to the database")
            return False
        return True

    async def load(self, key: str) -> str:
        # Load data from database
        try:
            r = db[key]
        except:
            log.warning(f"Unable to load requested data from the database, Key: {key} {type(key)}")
            return None
        #log.debug(f"Loaded data from database, Key: {key}")
        return r

    async def dump(self, key: str, value: Any) -> bool:
        # Dump data to database
        try:
            db[key] = value
        except Exception as e:
            log.warning(
                str(
                    f"Unable to dump data\n"
                    f"Key: {key} {type(key)}\n"
                    f"Value: {value} {type(value)}\n"
                    f"with an error: \n{e}"
                )
            )
            return False
        return True
    
    def loads(self, key: str) -> str:
        # Load data from database
        try:
            r = db[key]
        except:
            log.warning(f"Unable to load requested data from the database, Key: {key} {type(key)}")
            return None
        #log.debug(f"Loaded data from database, Key: {key}")
        return r

    def dumps(self, key: str, value: Any) -> bool:
        # Dump data to database
        try:
            db[key] = value
        except Exception as e:
            log.warning(
                str(
                    f"Unable to dump data\n"
                    f"Key: {key} {type(key)}\n"
                    f"Value: {value} {type(value)}\n"
                    f"with an error: \n{e}"
                )
            )
            return False
        return True