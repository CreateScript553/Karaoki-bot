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

# Веб-сервер для поддержки статуса Live на Render
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app_flask.run(host='0.0.0.0', port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши в любом чате @имя_твоего_бота и название песни, чтобы найти текст!")

# Функция инлайн-поиска (работает в любых чатах и с друзьями)
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return

    results = [
        InlineQueryResultArticle(
            id=query,
            title=f"Караоке: {query}",
            input_message_content=InputTextMessageContent(
                message_text=f"🎵 Текст и музыка для песни: *{query}* \n\n(Здесь скоро будет текст песни и караоке)",
                parse_mode="Markdown"
            ),
            description=f"Найти текст и музыку для '{query}'"
        )
    ]
    await update.inline_query.answer(results)

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
