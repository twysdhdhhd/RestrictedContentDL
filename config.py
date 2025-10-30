import os
from time import time
from dotenv import load_dotenv

load_dotenv("config.env", override=False)

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("SESSION_STRING")

if not BOT_TOKEN or ":" not in BOT_TOKEN:
    print("Error: BOT_TOKEN must be in format '123456:abcdefghijklmnopqrstuvwxyz'")
    exit(1)

if not SESSION_STRING or SESSION_STRING.startswith("x"):
    print("Error: SESSION_STRING must be a valid Pyrogram session string")
    exit(1)

class PyroConf:
    API_ID = int(API_ID)
    API_HASH = API_HASH
    BOT_TOKEN = BOT_TOKEN
    SESSION_STRING = SESSION_STRING
    BOT_START_TIME = time()
