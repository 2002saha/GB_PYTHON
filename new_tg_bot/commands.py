from config import dp, bot
from aiogram import types
from keyboards import menu_key, coin_key
import random
import csv
import logging
logging.basicConfig(level=logging.INFO)

total = 0


@dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    user_id = message.from_user.id
    user_login = message.from_user.username
    user_time = message.date.strftime("%Y-%m-%d %H:%M:%S")
    with open("new_tg_bot\logs\log.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user_id, user_login, user_time])
    print(message)
    print(message.from_user.id)
    await message.reply(f'✌️Привет, {message.from_user.first_name}!✌️')
    print('Start')
    await message.answer(f"💡Я знаю такие команды:💡\n\n/help и /start - справка по командам🤔\n\n/candy - игра в конфетки🍬\n\n/info - информация об проекте")
    await message.reply('✨Выбери команду✨', reply_markup=menu_key.kb_menu)
@dp.message_handler(commands='info')
async def info(message: types.Message):
    await message.reply(f'Это мой первый бот-игр в ТГ.\n\nСоздал: Алексадр Полежаев (@typec2)\n\nСпасибо, что попробовали мою разработку!')
    await message.reply('✨Выбери команду✨', reply_markup=menu_key.kb_menu)

@dp.message_handler(commands='candy')
async def candy_start_bot(message: types.Message):
    global total
    total = 150
    print('Бой начался')
    await message.reply(f'🦾Привет, {message.from_user.first_name}!\n\nДавай сыграем в конфетки cо Skynet.\n\n🍬На столе лежит {total} конфет.🍬\n\nМожно брать от 1 до 28 за раз. Кто взял последнюю, тот и победил.🤖')
    await message.answer(f'🪙Давай подбросим монетку🪙\n\nВыбирай: /орел или /решка?🤔', reply_markup=coin_key.kb_coin)

@dp.message_handler(commands= ['орел', 'решка'])
async def orel_reshka(message: types.Message):
    global total
    total = 150
    coin_random = random.choice(['орел', 'решка'])
    await message.answer(f'⁉️Сейчас подброшу монетку⁉️\n\nВыпал: {coin_random.capitalize()}!')
    if message.text[1:] == coin_random:
        await message.reply( f'😎Победа, {message.from_user.first_name}!😎\n\nТы ходишь первым!')
    else:
        await message.reply(f'Не повезло тебе, {message.from_user.first_name}!\n\n🤖Первым хожу я🤖')
        bot_take = random.randint(1, 28)
        total -= bot_take
        await message.answer(f'🤖Skynet взял {bot_take} конфет и осталось {total}.🤖')


@dp.message_handler()
async def candy_bot(message: types.Message):
    global total
    if message.text.isdigit():
        if total <= 0:
            await message.reply(f'{message.from_user.first_name}, '
                                f'а конфет нет! Если хочешь, сыграть пиши /candy')
        else:
            take = int(message.text)
            print(f'🤔{message.from_user.first_name} взял {take}🍬')
            if take < 1 or take > 28 or take > total:
                await message.reply(f'{message.from_user.first_name}, не жульничай!⚠️')
            else:
                total -= take
                if total == 0:
                    await message.reply(f'🤔{message.from_user.first_name}, '
                                    f'взял {take} конфет и осталось {total}.🍬')
                    await message.reply(f'🎊ПОБЕДА!🎊\n\nТы спас человечество от Skynet! Вернуть тебя в прошлое?🤔', reply_markup=menu_key.kb_menu)

                else:
                    await message.reply(f'🤔{message.from_user.first_name}, '
                                        f'взял {take} конфет и осталось {total}.🍬')
                    bot_take = 0
                    if total < 29:
                        bot_take = total
                    else:
                        bot_take = random.randint(1, 28)
                    total -= bot_take
                    if total == 0:
                        await message.answer(f'🤖Skynet взял {bot_take} конфет и осталось {total}.🍬')
                        await message.answer(f'🔥ТЫ ПРОИГРАЛ!🔥\n\n🤖Skynet победил, человечество пало перед искусственныи интелектом...🤖')
                        await message.reply('🤔Я могу тебя вернуть в прошлое, сделать это?🤔', reply_markup=menu_key.kb_menu)
                    else:
                        await message.answer(f'🤖Skynet взял {bot_take} конфет и осталось {total}.🍬')
    else:
        await message.reply(f'{message.from_user.first_name}, давай-ка цифрами🔢')


@dp.message_handler()
async def all_bot(message: types.Message):
    print(message)
    print('All')
    await message.reply(f'{message.from_user.first_name}, давай лучше сыграем в конфетки! Пиши /candy')