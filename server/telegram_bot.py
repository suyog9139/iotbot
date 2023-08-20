from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext  # Import necessary classes
import requests

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your temperature bot. Use /get_temperature to get the latest temperature.")

def get_temperature(update: Update, context: CallbackContext) -> None:
    response = requests.get("http://127.0.0.1:8000/latest-temperature/")
    if response.status_code == 200:
        data = response.json()
        latest_temperature = data.get("latest_temperature")
        if latest_temperature is not None:
            update.message.reply_text(f"The latest temperature is: {latest_temperature}°C")
        else:
            update.message.reply_text("Unable to fetch the latest temperature.")
    else:
        update.message.reply_text("Unable to fetch the latest temperature.")

def run_bot(token):
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("get_temperature", get_temperature))

    updater.start_polling()

if __name__ == "__main__":
    token = "6600979703:AAGvzsf4sdOgc3MbVEs2udVoNIj_vBWOpk4"
    run_bot(token)
