import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Привет, {user_name}! Бот успешно запущен и работает 24/7.")

def main():
    # Токен твоего бота
    TOKEN = "8733379913:AAE2gHOI8Vjqf_THYz83dyuK62hxTIN4R_c"

    # Создаем приложение бота
    app = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем команду /start
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
