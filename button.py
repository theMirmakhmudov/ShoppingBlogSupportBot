from aiogram import types

kb = [
    [types.KeyboardButton(text="Muammo yozib qoldirish 📝")]
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

phone = [
    [types.KeyboardButton(text="Contact yuborish", request_contact=True)]
]
contact = types.ReplyKeyboardMarkup(keyboard=phone, resize_keyboard=True)
