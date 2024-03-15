import logging
import asyncio
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from handler import *

load_dotenv(".env")
TOKEN = os.getenv("Token")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
router = Router()
dp.include_router(router)


async def main():
    dp.message.register(start, Command("start"))
    dp.message.register(feedback, F.text == "Muammo yozib qoldirish 📝")
    dp.message.register(phone, F.contact)
    dp.message.register(feedback2, Form.product_type)
    dp.message.register(feedback3, Form.product_name)
    dp.message.register(feedback4, Form.product_price)
    dp.message.register(finish, Form.feedback)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", )
    asyncio.run(main())
