import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, InlineQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Веб-сервер для Render
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app_flask.run(host='0.0.0.0', port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот готов к работе в чатах через инлайн-режим.")

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    
    # Если ничего не введено, выдаем базовую подсказку
    if not query:
        results = [
            InlineQueryResultArticle(
                id="help",
                title="Введите название песни",
                input_message_content=InputTextMessageContent(
                    message_text="Напишите после @Muzachik_bot название песни, чтобы найти караоке."
                ),
                description="Например: Леди Баг или Моника"
            )
        ]
    else:
        results = [
            InlineQueryResultArticle(
                id=query,
                title=f"Найти: {query}",
                input_message_content=InputTextMessageContent(
                    message_text=f"🎵 Запрос на песню: *{query}*",
                    parse_mode="Markdown"
                ),
                description=f"Нажми, чтобы отправить запрос: {query}"
            )
        ]
        
    await update.inline_query.answer(results, cache_time=1)

def main():
    server_thread = Thread(target=run_web)
    server_thread.start()

    TOKEN = "8733379913:AAE2gHOI8Vjqf_THYz83dyuK62hxTIN4R_c"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(InlineQueryHandler(inline_query))

    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
