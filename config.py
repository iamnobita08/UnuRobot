import os
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", 23343216))
API_HASH = os.environ.get("API_HASH", "1d66f21cd828dc22b80e3750719bd94a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Optional settings
MIN_PLAYERS = int(os.environ.get("MIN_PLAYERS", 2))
TIMEOUT = int(os.environ.get("TIMEOUT", 60))

bot = Client(
    "uno_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
# config.py

games = {}
player_game = {}
sudoers = [5536473064]  # Apna Telegram ID yaha daalo

timeout = 60  # default timeout in seconds (ya jitna code me chahiye)
