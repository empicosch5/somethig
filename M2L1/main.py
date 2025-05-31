import telebot
import os
import random

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7896634459:AAEzdxiT-uwTxx4AHl_SJB4I7boaMApJkHM")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)



# Запуск бота
bot.polling()