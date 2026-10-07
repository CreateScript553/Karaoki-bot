import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Создаем простой веб-сервер для Render, чтобы он не выдавал ошибку деплоя
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app_flask.run(host='0.0.0.0', port=10000)

# Логика Telegram бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне название песни, и я найду текст и музыку для караоке.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Ищу песню и текст по твоему запросу: «{text}»...")

def main():
    # Запускаем веб-сервер в отдельном потоке
    server_thread = Thread(target=run_web)
    server_thread.start()

    # Токен твоего бота
    TOKEN = "8733379913:AAE2gHOI8Vjqf_THYz83dyuK62hxTIN4R_c"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
