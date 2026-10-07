import os
import logging
import asyncio
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(level=logging.INFO)

app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app_flask.run(host='0.0.0.0', port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎤 Привет! Отправь мне название песни, и я начну отправлять слова караоке с задержкой по очереди!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song_name = update.message.text.strip()
    
    await update.message.reply_text(f"🎵 Начинаем караоке для песни: *{song_name}* 🎤", parse_mode="Markdown")
    
    # Пример строчек песни (позже заменим на реальный поиск из интернета или базы)
    sample_lyrics = [
        "🎶 Вспышка молнии в ночи...",
        "🎶 Светят звезды, ты кричи...",
        "🎶 Это песня для души...",
        "🎶 Пой со мной и не спеши!",
        "✨ Конец песни! Ставьте лайк боту! ✨"
    ]
    
    # Отправляем каждую строчку с задержкой в 3 секунды
    for line in sample_lyrics:
        await asyncio.sleep(3) # Задержка 3 секунды
        await update.message.reply_text(line)

def main():
    Thread(target=run_web).start()
    
    TOKEN = "8733379913:AAE2gHOI8Vjqf_THYz83dyuK62hxTIN4R_c"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    app.run_polling()

if __name__ == '__main__':
    main()
