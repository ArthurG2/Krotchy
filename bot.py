import random
import time
import telebot, wikipedia
from telebot import types
import random
bot = telebot.TeleBot('5919076405:AAGE_oKLTSnMbmNlCnyl_9whEwZSNiMUtNQ')
wikipedia.set_lang("ru")
def Krotchy(s):
    try:
        slovo = wikipedia.page(s)
        wikitext=slovo.content[:700]
        wiki=wikitext.split('.')
        wiki=wiki[:-1]
        wikitext1 = ''
        for x in wiki:
            if not('==' in x):
                if (len((x.strip())) > 2):
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
    keyboard2=types.KeyboardButton('Как дела, Кротчи?')
    markup.add(keyboard1,keyboard2)
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}, меня зовут Кротчи и я помогу тебе не чувствовать себя тупым. Введи любое слово, а я найду его значение в википедии', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    list = ["Орёл", "Решка"]
    list1=['Всё отлично, служу народу! =)',' Cегодня как-то грустно, спроси у меня что-нибудь, сразу станет лучше!']
    if message.text!='Орёл или решка' and  message.text!='Как дела, Кротчи?': bot.send_message(message.chat.id, Krotchy(message.text))
    elif message.text=='Орёл или решка':
        bot.send_message(message.chat.id, random.choice(list))
    elif message.text=='Как дела, Кротчи?':
        bot.send_message(message.chat.id, random.choice(list1))
bot.polling(none_stop=True, interval=0)