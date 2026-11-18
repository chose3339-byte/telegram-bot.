import os
import telebot

# يجلب التوكن تلقائياً من المتغيرات في Railway
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  bot.reply_to(
      message, "أهلاً بك! البوت يعمل بنجاح 24/7 على Railway 🚀"
  )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, f"أرسلت لي: {message.text}")


print("Bot is running...")
bot.infinity_polling()
