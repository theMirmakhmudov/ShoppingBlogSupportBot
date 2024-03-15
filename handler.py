from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import types
from button import keyboard, contact
from dotenv import load_dotenv
import os
from main import Bot

load_dotenv(".env")
Admin = os.getenv("Admin")


class Form(StatesGroup):
    phone = State()
    product_type = State()
    product_name = State()
    product_price = State()
    feedback = State()
    finish = State()


async def start(message: types.Message):
    await message.answer(
        f"<b>Assalomu Alaykum. Hurmatli {message.from_user.full_name}\nShoppingBlog support botiga xush kelibsiz.!</b>",
        reply_markup=keyboard)


async def feedback(message: types.Message, state: FSMContext):
    await state.set_state(Form.product_type)
    await message.answer("<b>Telefon raqamingizni kiriting:</b>", reply_markup=contact)  # noqa


async def phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(Form.product_type)
    await message.answer("<b>Mahsulot turini kiriting:</b>", reply_markup=ReplyKeyboardRemove())  # noqa


async def feedback2(message: types.Message, state: FSMContext):
    await state.update_data(product_type=message.text)
    await state.set_state(Form.product_name)
    await message.answer("<b>Mahsulot nomini kiriting:</b>")  # noqa


async def feedback3(message: types.Message, state: FSMContext):
    await state.update_data(product_name=message.text)
    await state.set_state(Form.product_price)
    await message.answer("Mahsulotni qanchaga sotib olganingizni kiriting:")  # noqa


async def feedback4(message: types.Message, state: FSMContext):
    await state.update_data(product_price=message.text)
    await state.set_state(Form.feedback)
    await message.answer("<b>Mahsulotda qanday muammo bo'layotganini yozing</b>")  # noqa


async def finish(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(feedback=message.text)
    await state.set_state(Form.finish)
    await message.answer("<b>Arizangiz qabul qilindi.\nAdminlarimiz tez orada aloqaga chiqadi!</b>")  # noqa
    data = await state.get_data()
    await state.clear()
    phone = data.get("phone", "Unknown")
    product_type = data.get("product_type", "Unknown")
    product_name = data.get("product_name", "Unknown")
    product_price = data.get("product_price", "Unknown")
    feedbacks = data.get("feedback", "Unknown")
    msg = f"<b>F.I.SH: {message.from_user.mention_html()}\nTelefon raqami: {phone}\nMahsulot turi: {product_type}\nMahsulot nomi: {product_name}\nMahsulot narxi: {product_price}\nMahsulot muammosi: {feedbacks}</b>"

    await bot.send_message(Admin, msg)
