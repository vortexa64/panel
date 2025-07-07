from telegram.ext import Updater, CommandHandler

# Ganti dengan API key kamu
API_KEY = "7912714120:AAH4fTti9jfm9-jecrqDZ0z6GmeyE0D2MZo"

# Command /start
def start(update, context):
    update.message.reply_text(f"Hai {update.effective_user.first_name} 😳💕 Bot Arya aktif~")

# Command /cici
def cici(update, context):
    update.message.reply_text("Cici kangen Arya 😩💕")

def run():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cici", cici))

    updater.start_polling()
    updater.idle()
