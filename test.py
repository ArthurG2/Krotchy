import pytest
from unittest.mock import Mock
import telebot
import random

import bot


def test_start():

    telebot.TeleBot.send_message = Mock()
    telebot.types.ReplyKeyboardMarkup = Mock()
    message = Mock()
    message.text = '/start'
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1 = telebot.types.KeyboardButton('Орёл или решка')
    keyboard2 = telebot.types.KeyboardButton('Поддержи меня')
    keyboard3 = telebot.types.KeyboardButton('Интересный факт')
    keyboard4 = telebot.types.KeyboardButton('Игры')
    markup.add(keyboard1, keyboard2, keyboard3, keyboard4)
    bot.start(message)
    bot.bot.send_message.assert_called_with(message.chat.id,
                                            f'Привет, {message.chat.first_name}, меня зовут Кротчи и я помогу тебе не чувствовать себя тупым. Введи любое слово, а я найду его значение в википедии. Так же можешь попросить рассказать интересный факт, коих я знаю немало.',
                                            reply_markup=markup)


def test_handle_text():
    telebot.TeleBot.send_message = Mock()
    bot.knbb = Mock()
    bot.knbn = Mock()
    bot.knbk = Mock()
    bot.knbb.return_value = 'Бумага'
    bot.knbn.return_value = 'Ножницы'
    bot.knbk.return_value = 'Камень'
    bot.Krotchy = Mock()
    random.choice = Mock()
    random.choice.return_value = "Test"
    open = Mock()
    list = ["Орёл", "Решка"]
    actions = ['bad message', 'Орёл или решка', 'Интересный факт', 'Поддержи меня', 'Правда', 'Действие', 'Камень',
               'Ножницы', 'Бумага']
    results = [bot.Krotchy("bad message"),
               "Test",
               'Факт№Test',
               'Test',
               'Test',
               'Test',
               'Камень',
               'Ножницы',
               'Бумага'
               ]
    for i in range(len(actions)):
        message = Mock()
        message.text = actions[i]
        bot.handle_text(message)
        bot.bot.send_message.assert_called_with(message.chat.id, results[i])


def test_menu():
    telebot.TeleBot.send_message = Mock()
    bot.start = Mock()
    message = Mock()
    message.text = 'Меню'
    bot.handle_text(message)
    bot.start.assert_called_with(message)


def test_kmn():
    telebot.TeleBot.send_message = Mock()
    telebot.types.ReplyKeyboardMarkup = Mock()
    message = Mock()
    message.text = 'КМН(с Кротчи)'
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard9 = telebot.types.KeyboardButton('Камень')
    keyboard10 = telebot.types.KeyboardButton('Ножницы')
    keyboard11 = telebot.types.KeyboardButton('Бумага')
    keyboard20 = telebot.types.KeyboardButton('Меню')
    markup.add(keyboard9, keyboard10, keyboard11, keyboard20)
    bot.handle_text(message)
    bot.bot.send_message.assert_called_with(message.chat.id, 'Ну давай поиграем ахахахах)', reply_markup=markup)


def test_games():
    telebot.TeleBot.send_message = Mock()
    telebot.types.ReplyKeyboardMarkup = Mock()
    message = Mock()
    message.text = 'Игры'
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard5 = telebot.types.KeyboardButton('Правда или действие')
    keyboard6 = telebot.types.KeyboardButton('КМН(с Кротчи)')
    keyboard20 = telebot.types.KeyboardButton('Меню')
    markup.add(keyboard5, keyboard6, keyboard20)
    bot.handle_text(message)
    bot.bot.send_message.assert_called_with(message.chat.id, f' {message.chat.first_name}, во что играть будем?',
                                            reply_markup=markup)


def test_truth_or_action():
    telebot.TeleBot.send_message = Mock()
    telebot.types.ReplyKeyboardMarkup = Mock()
    message = Mock()
    message.text = 'Правда или действие'
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard7 = telebot.types.KeyboardButton('Правда')
    keyboard8 = telebot.types.KeyboardButton('Действие')
    keyboard20 = telebot.types.KeyboardButton('Меню')
    markup.add(keyboard7, keyboard8, keyboard20)
    bot.handle_text(message)
    bot.bot.send_message.assert_called_with(message.chat.id, 'Выбирай =)', reply_markup=markup)