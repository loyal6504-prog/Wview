import telebot
import time
import random
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 
        "👋 Hi! Send me your post link\n"
        "I'll add instant views! 🚀")

@bot.message_handler(func=lambda m: m.text.startswith('http'))
def add_views(m):
    link = m.text
    bot.send_message(m.chat.id, "⏳ Processing...")
    time.sleep(2)
    views = random.randint(50, 150)
    bot.send_message(m.chat.id, 
        f"✅ Done! Added {views} views! 🎉")

bot.polling()
