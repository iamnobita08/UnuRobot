import os

API_ID = int(os.environ.get("API_ID", 23343216))
API_HASH = os.environ.get("API_HASH", "1d66f21cd828dc22b80e3750719bd94a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")

# Optional settings
MIN_PLAYERS = int(os.environ.get("MIN_PLAYERS", 2))
TIMEOUT = int(os.environ.get("TIMEOUT", 60))
