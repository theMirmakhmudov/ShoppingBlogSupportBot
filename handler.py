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


class Idea(StatesGroup):
    fullname = State()
    phone = State()
    idea = State()
    finish = State()


async def start(message: types.Message):
    await message.answer(
        f"<b>Assalomu Alaykum. Hurmatli {message.from_user.full_name}\nShoppingBlog support botiga xush kelibsiz.!</b>",
        reply_markup=keyboard)


async def idea(message: types.Message, state: FSMContext):
    await state.set_state(Idea.fullname)
    await message.answer("<b>Biz sizni taniy olishimiz uchun to'liq ism familiyangizni kiriting: </b>")


async def fullname(message: types.Message, state: FSMContext):
    await state.update_data(fullname_idea=message.text)
    await state.set_state(Idea.phone)
    await message.answer("<b>Contact yuboring</b>", reply_markup=contact)


async def phone(message: types.Message, state: FSMContext):
    await state.update_data(phone_idea=message.contact.phone_number)
    await state.set_state(Idea.idea)
    await message.answer("<b>Savol yoki Taklifingizni yozing 📝</b>")


async def ideas(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(idea=message.text)
    await state.set_state(Idea.finish)
    await message.answer("Savol va Takliflaringiz adminga yuborildi ✅")
    idea_data = await state.get_data()
    await state.clear()
    fullname_idea = idea_data.get("fullname_idea", "Unknown")
    phone_idea = idea_data.get("phone_idea", "Unknown")
    ideas = idea_data.get("idea", "Unknown")
    await message.answer("Yuborildi ✅")
    msg = f"""<b>
Savol va Takliflar 💡
🧔🏻‍♂️ To'liq ismi: {fullname_idea}
📱 Telefon raqami: {phone_idea}
💡 Savol va Taklifi: {ideas}    
</b>"""
    await bot.send_message(Admin, msg)


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
    msg = f"""<b>
Mahsulotdagi muammo 🔧
🧔🏻‍♂️ F.I.SH: {message.from_user.full_name}
📲 Telefon raqami: {phone}
🧸 Mahsulot turi: {product_type}
🛍 Mahsulot nomi: {product_name}
💴 Mahsulot narxi: {product_price}
🔧 Mahsulotdagi muammo: {feedbacks}
   </b>"""

    await bot.send_message(Admin, msg)
