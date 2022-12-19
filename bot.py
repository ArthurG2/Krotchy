import random
import time
import telebot, wikipedia
from telebot import types
import random
bot = telebot.TeleBot('5919076405:AAGE_oKLTSnMbmNlCnyl_9whEwZSNiMUtNQ') ## API Токен бота
wikipedia.set_lang("ru") ##выбор языка
def Krotchy(s): ##ввод ффункции
    try:
        slovo = wikipedia.page(s) 
        wikitext=slovo.content[:700] ##читает всё до 700 знака
        wiki=wikitext.split('.') ##разделяет между собой предложения
        wiki=wiki[:-1] ## отбрасывает все что идёт после последней вышедшей точки
        wikitext1 = '' ##ввод переменной, куда всё будет считываться
        for x in wiki:
            if not('==' in x): ##начинает читать всё кроме заголовка
                    wikitext1+=x
            else:
                break
        return wikitext1
    except Exception as e:
        return 'Ну ты и спросил, дружище... С этим я тебе помочь не смогу, прости :_(' ## вывод фразы в том случае, если статьи на википедии по этому запросу нет
@bot.message_handler(commands=["start"])
def start(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True) ##назначение клавиатуры (кнопки снизу)
    keyboard1=types.KeyboardButton('Орёл или решка') ##кнопка №1
    keyboard2=types.KeyboardButton('Как дела, Кротчи?') ##кнопка №2
    markup.add(keyboard1,keyboard2) ##добавляем эти кнопки 
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}, меня зовут Кротчи и я помогу тебе не чувствовать себя тупым. Введи любое слово, а я найду его значение в википедии', reply_markup=markup)
## говорим что делать боту при команде start
@bot.message_handler(content_types=["text"]) ## если на вход поступает текст, то
def handle_text(message):
    list = ["Орёл", "Решка"] ## это понадобится позже
    list1=['Всё отлично, служу народу! =)',' Cегодня как-то грустно, спроси у меня что-нибудь, сразу станет лучше!'] ## это тоже
    if message.text!='Орёл или решка' and  message.text!='Как дела, Кротчи?': 
        bot.send_message(message.chat.id, Krotchy(message.text)) ## если запрос слова не похож на те, что используются в дополнительной клавиатуре, то бот вставляет статью из википедии
    elif message.text=='Орёл или решка': ## если строчка похожа на строчку из доп. клавиатуры, то он "подкидывает монету", путем случайного выбор даёт ответ
        bot.send_message(message.chat.id, random.choice(list))
    elif message.text=='Как дела, Кротчи?': ## если нажимают на вторую кнопку, бот вежливо отвечает собеседнику как он себя чувствует. сделано ради разнообразия
        bot.send_message(message.chat.id, random.choice(list1))
bot.polling(none_stop=True, interval=0) ##запуск бота
