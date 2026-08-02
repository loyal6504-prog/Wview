# main.py
import telebot
import time
import random
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN not set - add BOT_TOKEN in Railway Variables")
    raise SystemExit("BOT_TOKEN missing")

print("Starting bot...")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "👋 Hi! Send me your post link. I'll add instant views! 🚀")

@bot.message_handler(func=lambda m: m.text and m.text.startswith('http'))
def add_views(m):
    link = m.text
    print("Received link from", getattr(m.from_user, "username", m.from_user.id), "->", link)
    bot.send_message(m.chat.id, "⏳ Processing...")
    time.sleep(2)
    views = random.randint(50, 150)
    bot.send_message(m.chat.id, f"✅ Done! Added {views} views! 🎉")
    print("Added", views, "views for", link)

try:
    print("Bot polling now...")
    bot.polling(none_stop=True)
except Exception as e:
    print("Polling error:", e)
    
