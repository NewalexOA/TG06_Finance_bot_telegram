import random
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import F


async def send_tips(message: Message):
    tips = [
        "Совет 1: Ведите бюджет и следите за своими расходами.",
        "Совет 2: Откладывайте часть доходов на сбережения.",
        "Совет 3: Покупайте товары по скидкам и распродажам."
    ]
    tip = random.choice(tips)
    await message.answer(tip)


def register_handlers(dp: Dispatcher):
    dp.message.register(send_tips, F.text == "Советы по экономии")
