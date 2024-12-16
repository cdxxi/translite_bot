import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, filename='mylog.log')

def translite(x):
    trvoc = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'ъ': 'ie', 'ь':'', 'э': 'e', 'ю': 'iu', 'я': 'ia'}
    res = ''
    for i in x.lower():
        if i.isalpha() and i in trvoc.keys():
            res+=trvoc[i]
        else:
            res+=i
    return res.title()


@dp.message(Command(commands=['start']))
async def process_comand_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_translite(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = translite(message.text)
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=text)

if __name__ == '__main__':
    dp.run_polling(bot) 