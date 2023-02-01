import asyncio
from aiogram import Bot, Dispatcher, executor, types
import random
from aiogram.types import Message

API_TOKEN = '5681968815:AAFWpak4Esu4TcP-3o1myte_UmtlvCLwPWc'

# Configure logging
import logging

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    await bot.send_message(
        message.from_user.id, 
        "👋 Привет! Я первый бот-игра Александра Полежаева!", 
        reply_markup=markup
    )
    await bot.send_message(
        message.from_user.id, 
        "🍬Добро пожаловать в 'Конфетную игру'!🍬", 
        reply_markup=markup
    )

@dp.message_handler(content_types=['text'])
async def get_text_messages(message: types.Message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('👨2 игрока на одном телефоне👨')
        btn2 = types.KeyboardButton('Против ИИ')
        btn3 = types.KeyboardButton('❓Инфо❓')
        markup.add(btn1, btn2, btn3)
        await bot.send_message(
            message.from_user.id, 
            '❓ Выберите режим игры ❓', 
            reply_markup=markup
        )

    elif message.text == '👨2 игрока на одном телефоне👨':
        await bot.send_message(
            message.from_user.id, 
            "В разработке..",
            parse_mode='Markdown'
        )
    elif message.text == 'Против ИИ':
        await bot.send_message(
            message.from_user.id, 
            "В разработке..",
            parse_mode='Markdown'
    
    elif message.text == '❓Инфо❓':
        await bot.send_message(
            message.from_user.id, 
            "🎮 На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 🎮",
            parse_mode='Markdown'
        )

executor.start_polling(dp, skip_updates=True)