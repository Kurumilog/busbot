import telebot
from telebot import types
from datetime import datetime


bot = telebot.TeleBot('7535209407:AAEeMGeo-RBPe6HltSuSuLqDoJ0TiMyGA58')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,  'Здравствуй, я твой личный помощник Healthbot. Выбери, что тебе надо', reply_markup=markup)
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Напоминание пить воду')
    btn2 = types.KeyboardButton('Рассчитать свой рост')
    btn3 = types.KeyboardButton('Заполнить профиль')
    markup.row(btn1, btn2)


bot.polling()