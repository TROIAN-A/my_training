# -*- coding: utf-8 -*-
import telebot
from telebot import types

TOKEN = '1283121145:AAHmDu8ZlQTvDPo5iCFbAaKpOIBIxb_36UE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Привет', 'Пока', '1', '3')
    markup.row('1', '2')
    markup.row('3', '4')
    bot.send_message(message.chat.id, 'Привет человек', reply_markup=markup)


@bot.message_handler(commands=['inline'])
def inline(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Привет бот', callback_data='hi')
    item2 = types.InlineKeyboardButton('Пока', callback_data='hi1')
    item3 = types.InlineKeyboardButton('1', callback_data='hi2')
    item4 = types.InlineKeyboardButton('2', callback_data='hi3')
    item5 = types.InlineKeyboardButton('3', callback_data='hi4')
    markup.add(item, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def data(call):
    if call.message:
        if call.data == 'hi':
            bot.send_message(call.message.chat.id, 'Привет друг')
        elif call.data == 'hi1':
            bot.send_message(call.message.chat.id, 'Пока друг')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет,привет!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Пока!')


bot.polling()
