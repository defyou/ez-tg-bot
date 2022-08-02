import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from dataclasses import dataclass
from typing import List
from aiogram.types import LabeledPrice


BOT_TOKEN = '5422030401:AAF5WqpONaAWzWxMltVtVbeOyF4hzqLTbY0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

button1 = KeyboardButton('Курсы')
start_b = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_b.add(button1)

button_oga = KeyboardButton('Подготовка к ОГЭ')
button_ega = KeyboardButton('Подготовка к ЕГЭ')
ogaega = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
ogaega.add(button_oga)
ogaega.add(button_ega)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('🐱 Добро пожаловать! 🐱\n'
                        '🐱Вы хотите научиться делать телеграмм ботов?🐱\n'
                        '🐱Заходите в курсы и приобретайте понравившиеся вам!🐱', reply_markup=start_b)

@dp.message_handler(text='Курсы')
async def oga_command(message: types.Message):
    await message.answer('Выбирайте', reply_markup=ogaega)


@dp.message_handler(text='Подготовка к ОГЭ')
async def oga_command(message: types.Message):
    await message.reply('Вот файлы для подготовки основных предметов по ОГЭ')
    await message.answer_document('http://doc.fipi.ru/o-nas/novosti/metodicheskiye-rekomendatsii-po-samostoyatelnoy-podgotovke-k-oge/matematika-oge.pdf')
    await message.answer_document('http://doc.fipi.ru/o-nas/novosti/metodicheskiye-rekomendatsii-po-samostoyatelnoy-podgotovke-k-oge/russkiy-yazyk-oge.pdf')

@dp.message_handler(text='Подготовка к ЕГЭ')
async def ega_command(message: types.Message):
    await message.reply('Вот файлы для подготовки основных предметов по ЕГЭ')
    await message.answer_document('http://doc.fipi.ru/navigator-podgotovki/navigator-ege/Mat_prof.pdf')
    await message.answer_document('http://doc.fipi.ru/metodicheskaya-kopilka/metod-rekomendatsii-dlya-vypusknikov-po-sam-podgotovke-k-ekzamenam/russkiy-yazyk.pdf')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)