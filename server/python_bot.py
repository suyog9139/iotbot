import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram Bot Token (replace with your actual bot token)
BOT_TOKEN = "6600979703:AAGvzsf4sdOgc3MbVEs2udVoNIj_vBWOpk4"

# Base URL of your Django server
BASE_URL = "http://127.0.0.1:8000"

# Command handler for /latest_temperature command
def latest_temperature(update: Update, context: CallbackContext) -> None:
    response = requests.get(BASE_URL + "/api/temperature-data/")
    if response.status_code == 200:
        data = response.json()
        temperature = data.get("temperature")
        if temperature is not None:
            update.message.reply_text(f"Latest temperature: {temperature} °C")
        else:
            update.message.reply_text("No temperature data available.")
    else:
        update.message.reply_text("Failed to fetch temperature data.")


def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"Hello {user.first_name}! I'm your temperature bot. Use /latest_temperature to get the latest temperature.")


def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the /latest_temperature command handler
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("latest_temperature", latest_temperature))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
