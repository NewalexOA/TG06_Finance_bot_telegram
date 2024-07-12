import requests
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import F


async def exchange_rates(message: Message):
    url = "https://v6.exchangerate-api.com/v6/09edf8b2bb246e1f801cbfba/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Это проверит статус код
        data = response.json()
        usd_to_rub = data['conversion_rates']['RUB']
        eur_to_usd = data['conversion_rates']['EUR']
        euro_to_rub = eur_to_usd * usd_to_rub
        await message.answer(f"1 USD - {usd_to_rub:.2f} RUB\n"
                             f"1 EUR - {euro_to_rub:.2f} RUB")
    except requests.RequestException:
        await message.answer("Не удалось получить данные о курсе валют!")


def register_handlers(dp: Dispatcher):
    dp.message.register(exchange_rates, F.text == "Курс валют")
