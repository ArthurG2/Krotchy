# -*- coding: utf8 -*-
import random
import time
import telebot, wikipedia
import os
from telebot import types
from google_currency import convert
import random
bot = telebot.TeleBot('5865494074:AAGsPfhoNy5E9ySXDLgHGYO2HJ_EYLAkkFI')
wikipedia.set_lang("ru")
file = open('Факты.txt')


def knbk(message):
    listkmn = ['Камень', 'Ножницы', 'Бумага']
    s=''
    d = random.choice(listkmn)
    if d == 'Камень':
        s='У меня камень. Пипец, дружище, Ничья 😔️'
    elif d == 'Бумага':
        s='У меня бумага. Легчайшая для меня победа, поднапрягись🤣️'
    elif d == 'Ножницы':
        s='У меня ножницы.Я проиграл😔️'
    return s
def knbn(message):
    listkmn = ['Камень', 'Ножницы', 'Бумага']
    s=''
    d = random.choice(listkmn)
    if d == 'Бумага':
        s='У меня бумага. Я проиграл😩️'
    elif d == 'Камень':
        s = 'У меня камень. Легчайшая для меня победа, поднапрягись🥱️'
    elif d == 'Ножницы':
        s='У меня ножницы. Пипец, дружище, Ничья 🤯'
    return s
def knbb(message):
    listkmn = ['Камень', 'Ножницы', 'Бумага']
    s=''
    d = random.choice(listkmn)
    if d == 'Камень':
        s='У меня камень.Я проиграл🤕️'
    elif d == 'Бумага':
        s='У меня бумага. Пипец, дружище, Ничья 🥶'
    elif d == 'Ножницы':
        s='У меня ножницы. Легчайшая для меня победа, поднапрягись😎️'
    return s
def Krotchy(s):
    try:
        slovo = wikipedia.page(s)
        wikitext=slovo.content[:700]
        wiki=wikitext.split('.')
        wiki=wiki[:-1]
        wikitext1 = ''
        for x in wiki:
            if not('==' in x):
                    wikitext1+=x
            else:
                break
        return wikitext1
    except Exception as e:
        return 'Ну ты и спросил, дружище... С этим я тебе помочь не смогу, прости :_('
@bot.message_handler(commands=["start"])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1=types.KeyboardButton('Орёл или решка')
    keyboard2=types.KeyboardButton('Поддержи меня')
    keyboard3 = types.KeyboardButton('Интересный факт')
    keyboard4 = types.KeyboardButton('Игры')
    markup.add(keyboard1,keyboard2,keyboard3,keyboard4)
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}, меня зовут Кротчи и я помогу тебе не чувствовать себя тупым. Введи любое слово, а я найду его значение в википедии. Так же можешь попросить рассказать интересный факт, коих я знаю немало.', reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    list = ["Орёл", "Решка"]
    list1=['Орёл или решка','Интересный факт','Поддержи меня','Меню','Игры', 'Правда или действие', 'Правда','Действие','КМН(с Кротчи','Камень','Ножницы','Бумага']
    if message.text not in list1:
        bot.send_message(message.chat.id, Krotchy(message.text))
    elif message.text=='Орёл или решка':
        bot.send_message(message.chat.id, random.choice(list))
    elif message.text == 'Интересный факт':
        with open("Фактики.txt", mode="r", encoding="utf-8") as r_file:
            file_text = r_file.readlines()
            text = random.choice(file_text)
        bot.send_message(message.chat.id, f'Факт№{text}')
    elif message.text == 'Поддержи меня':
        with open("Мотивация.txt", mode="r", encoding="utf-8") as r_file:
            file_text = r_file.readlines()
            text = random.choice(file_text)
        bot.send_message(message.chat.id, text)
    elif message.text == 'Игры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard5 = types.KeyboardButton('Правда или действие')
        keyboard6 = types.KeyboardButton('КМН(с Кротчи')
        keyboard20 = types.KeyboardButton('Меню')
        markup.add(keyboard5, keyboard6, keyboard20)
        bot.send_message(message.chat.id,f' {message.chat.first_name}, во что играть будем?', reply_markup=markup)
    elif message.text == 'Правда или действие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard7 = types.KeyboardButton('Правда')
        keyboard8 = types.KeyboardButton('Действие')
        keyboard20 = types.KeyboardButton('Меню')
        markup.add(keyboard7, keyboard8, keyboard20)
        bot.send_message(message.chat.id, 'Выбирай =)', reply_markup=markup)

    elif message.text=='Действие':
        with open("Действия.txt", mode="r", encoding="utf-8") as r_file:
            file_text = r_file.readlines()
            text = random.choice(file_text)
        bot.send_message(message.chat.id, text)
    elif message.text == 'Правда':
        with open("Правда.txt", mode="r", encoding="utf-8") as r_file:
            file_text = r_file.readlines()
            text = random.choice(file_text)
        bot.send_message(message.chat.id, text)
    elif message.text == 'КМН(с Кротчи':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard9 = types.KeyboardButton('Камень')
        keyboard10 = types.KeyboardButton('Ножницы')
        keyboard11 = types.KeyboardButton('Бумага')
        keyboard20 = types.KeyboardButton('Меню')
        markup.add(keyboard9, keyboard10, keyboard11,keyboard20)
        bot.send_message(message.chat.id, 'Ну давай поиграем ахахахах)', reply_markup=markup)
    elif message.text == 'Камень':
        bot.send_message(message.chat.id, knbk(message))
    elif message.text == 'Бумага':
        bot.send_message(message.chat.id, knbb(message))
    elif message.text == 'Ножницы':
        bot.send_message(message.chat.id, knbn(message))
    elif message.text == 'Меню':
        start(message)
bot.polling(none_stop=True, interval=0)
