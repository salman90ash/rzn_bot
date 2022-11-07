import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BOT_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
print(BOT_TOKEN)
