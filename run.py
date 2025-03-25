import asyncio
import logging

from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import F
from config import recipe
from get_cat import get_cat

bot = Bot(token=TOKEN)
dp = Dispatcher()

catboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='😱😍  Кота палучить да жи ес (кот в мешке) 🐈🇨🇮')]
], resize_keyboard=True)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Хуй)))', reply_markup=catboard)


@dp.message(Command('cat'))
async def send_cat(message: Message):
    img_url = get_cat()
    await message.answer_photo(img_url)



@dp.message(F.text == '😱😍  Кота палучить да жи ес (кот в мешке) 🐈🇨🇮')
async def send_cat(message: Message):
    img_url = get_cat()
    await message.answer_photo(img_url)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
