from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database import get_connection_and_cursor, close_connection


class FinancesForm(StatesGroup):
    category1 = State()
    expenses1 = State()
    category2 = State()
    expenses2 = State()
    category3 = State()
    expenses3 = State()


async def finances_start(message: Message, state: FSMContext):
    await state.set_state(FinancesForm.category1)
    await message.reply("Введите первую категорию расходов:")


async def finances_category1(message: Message, state: FSMContext):
    await state.update_data(category1=message.text)
    await state.set_state(FinancesForm.expenses1)
    await message.reply("Введите расходы для категории 1:")


async def finances_expenses1(message: Message, state: FSMContext):
    await state.update_data(expenses1=float(message.text))
    await state.set_state(FinancesForm.category2)
    await message.reply("Введите вторую категорию расходов:")


async def finances_category2(message: Message, state: FSMContext):
    await state.update_data(category2=message.text)
    await state.set_state(FinancesForm.expenses2)
    await message.reply("Введите расходы для категории 2:")


async def finances_expenses2(message: Message, state: FSMContext):
    await state.update_data(expenses2=float(message.text))
    await state.set_state(FinancesForm.category3)
    await message.reply("Введите третью категорию расходов:")


async def finances_category3(message: Message, state: FSMContext):
    await state.update_data(category3=message.text)
    await state.set_state(FinancesForm.expenses3)
    await message.reply("Введите расходы для категории 3:")


async def finances_expenses3(message: Message, state: FSMContext):
    data = await state.get_data()
    conn, cursor = get_connection_and_cursor()
    telegram_id = message.from_user.id
    cursor.execute('''
        UPDATE users SET category1 = ?, expenses1 = ?, category2 = ?, expenses2 = ?, category3 = ?, expenses3 = ? WHERE telegram_id = ?''',
                   (data['category1'], data['expenses1'], data['category2'], data['expenses2'], data['category3'],
                    float(message.text), telegram_id))
    conn.commit()
    await state.clear()
    await message.answer("Категории и расходы сохранены!")
    close_connection(conn)


def register_handlers(dp: Dispatcher):
    dp.message.register(finances_start, F.text == "Личные финансы")
    dp.message.register(finances_category1, FinancesForm.category1)
    dp.message.register(finances_expenses1, FinancesForm.expenses1)
    dp.message.register(finances_category2, FinancesForm.category2)
    dp.message.register(finances_expenses2, FinancesForm.expenses2)
    dp.message.register(finances_category3, FinancesForm.category3)
    dp.message.register(finances_expenses3, FinancesForm.expenses3)
