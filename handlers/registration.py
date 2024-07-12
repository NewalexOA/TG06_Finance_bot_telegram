from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import F
from database import get_connection_and_cursor, close_connection


async def registration(message: Message):
    conn, cursor = get_connection_and_cursor()
    telegram_id = message.from_user.id
    name = message.from_user.full_name
    cursor.execute('''SELECT * FROM users WHERE telegram_id = ?''', (telegram_id,))
    user = cursor.fetchone()
    if user:
        await message.answer("Вы уже зарегистрированы!")
    else:
        cursor.execute('''INSERT INTO users (telegram_id, name) VALUES (?, ?)''', (telegram_id, name))
        conn.commit()
        await message.answer("Вы успешно зарегистрированы!")
    close_connection(conn)


def register_handlers(dp: Dispatcher):
    dp.message.register(registration, F.text == "Регистрация в телеграм боте")
