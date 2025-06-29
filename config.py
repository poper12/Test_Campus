from dotenv import load_dotenv
import os

load_dotenv()

env_vars = {
  # Get From my.telegram.org
  "API_HASH": os.getenv("API_HASH", ""),
  # Get From my.telegram.org
  "API_ID": os.getenv("API_ID", ""),
  #Get For @BotFather
  "BOT_TOKEN": os.getenv("BOT_TOKEN", ""),
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "mongodb+srv://testingletsee:zwwpsYGUSaik5tXl@cluster0.wtvqre0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "Dump2075",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "[MC] [{chap_num}] {chap_name} @Manga_Campus"
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL')
