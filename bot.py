import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import registration, exchange_rates, tips, finances
from database import init_db, close_connection

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

# Инициализация базы данных
conn, cursor = init_db()

# Регистрация обработчиков
registration.register_handlers(dp)
exchange_rates.register_handlers(dp)
tips.register_handlers(dp)
finances.register_handlers(dp)


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        close_connection(conn)


if __name__ == '__main__':
    asyncio.run(main())
