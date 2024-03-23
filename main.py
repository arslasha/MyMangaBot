import telebot
from telebot import types

from config import TOKEN

import telebot
bot = telebot.TeleBot(TOKEN)

chatID = -1001551102382


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("❓ Что я читаю?")
    btn2 = types.KeyboardButton("📖 Выбрать мангу")
    btn3 = types.KeyboardButton("💡 Последние главы")

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, который создан для чтения манги! Если что-то непонятно, введи команду /help.".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "❓ Что я читаю?"):
        bot.send_message(message.chat.id, text="Список манги, которую ты читаешь: \n\n🀄Башня Бога \n🀄Ветролом \n🀄Всеведущий читатель \n🀄Возвращение железнокровной гончей \n🀄Гениальный убийца, который делает всё в одиночку \n🀄Игрок, который вернулся спустя 10000 лет \n🀄Невероятное обучение \n🀄Непобедимый. Проект «Ильджин» \n🀄Прирождённый наёмник \n🀄Пэк ХХ \n🀄Ранкер, который живёт второй раз \n🀄Регрессия с властью короля \n🀄Убийца Питер \n🀄Убить злодея")
    elif (message.text == "📖 Выбрать мангу"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🀄Башня Бога ")
        btn2 = types.KeyboardButton("🀄Ветролом")
        btn3 = types.KeyboardButton("🀄Возвращение железнокровной гончей")
        btn4 = types.KeyboardButton("🀄Невероятное обучение")
        btn5 = types.KeyboardButton("🀄Убить злодея")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(message.chat.id, text="Выбери мангу, которую хочешь прочитать.", reply_markup=markup)


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, 'Помощь')


@bot.message_handler(content_types=['photo', 'document', 'audio', 'video'])
def all_media_messages(message):
    if message.caption is not None and 'The Tutorial is Too Hard' in message.caption.lower():
        bot.forward_message(chatID, message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling(none_stop=True)