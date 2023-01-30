import telebot
from telebot import types
import random

bot = telebot.TeleBot('5681968815:AAFWpak4Esu4TcP-3o1myte_UmtlvCLwPWc')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я первый бот-игра Александра Полежаева!", reply_markup=markup)
    bot.send_message(message.from_user.id, "🍬Добро пожаловать в 'Конфетную игру'!🍬", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('👨2 игрока на одном телефоне👨')
        btn2 = types.KeyboardButton('Против ИИ')
        btn3 = types.KeyboardButton('❓Инфо❓')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Выберите режим игры ❓', reply_markup=markup) 


    elif message.text == '👨2 игрока на одном телефоне👨':
        bot.send_message(message.from_user.id, "В разработке..",parse_mode='Markdown')

    elif message.text == 'Против ИИ':
        start_game(message)

    elif message.text == '❓Инфо❓':
        bot.send_message(message.from_user.id, '🎮 На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 🎮',parse_mode='Markdown')

@bot.message_handler(commands=['text'])
def start_game(message):
    bot.send_message(chat_id=message.chat.id, text="Welcome to the candy game!\n")
    player1 = message.from_user.first_name
    player2 = "AI"
    candies = 100
    turn = random.choice([player1, player2])
    bot.send_message(chat_id=message.chat.id, text=f"\nPlayer: {turn} won the draw and will make the first move.\n")

    while candies > 0:
        if turn == player2:
            if candies <= 28:
                move = candies
            else:
                move = 1 + candies % 28
            bot.send_message(chat_id=message.chat.id, text=f"{turn} takes {move} candies.")
        else:
            bot.send_message(chat_id=message.chat.id, text=f"{turn} move.")
            move = bot.send_message(chat_id=message.chat.id, text="How many candies do you want to take (up to 28)? ")
            bot.register_next_step_handler (move, number)
            while move < 1 or move > 28 or move > candies:
                bot.send_message(chat_id=message.chat.id, text="Invalid move. Please enter a number from 1 to 28: ")
                bot.register_next_step_handler(move, number)
        candies -= move
        bot.send_message(chat_id=message.chat.id, text=f"{turn} takes {move} candies. {candies} candies left on the table.\n")
        if candies == 0:
            bot.send_message(chat_id=message.chat.id, text=f"{turn} won the game! Congratulations!")
            break
        if turn == player1:
            turn = player2
        else:
            turn = player1
def number(message):
    x = int(message.text) # Это и будет текст, которой отправил пользователь

bot.polling(none_stop=True, interval=0) 