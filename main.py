import telebot
import places
import random
from telebot import types 

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, я помогу тебе выбрать место для прогулки", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Москва")
        btn2 = types.KeyboardButton("Подмосковье")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Выбери куда ты хочешь поехать',reply_markup=markup)
        
    elif message.text == "Подмосковье":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Москва")
        btn2 = types.KeyboardButton("Подмосковье")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,back)
        bot.send_message(message.chat.id, text=f'Едь в {random.sample(places.zagorod,1)[0]}',reply_markup=markup)
    
    elif message.text == "Москва":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Москва")
        btn2 = types.KeyboardButton("Подмосковье")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2,back)
        bot.send_message(message.chat.id, text=f'Едь в {random.sample(places.moscow,1)[0]}',reply_markup=markup)
    
    elif (message.text == "Вернуться в главное меню"):
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         button1 = types.KeyboardButton("👋 Поздороваться")
         markup.add(button1)
         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
        
bot.polling(none_stop=True, interval=0)
