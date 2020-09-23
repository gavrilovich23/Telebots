import telebot
from telebot import types

bot = telebot.TeleBot('1205687194:AAEFhURp4sxVNSCpiFMY4iNTcNgNbHi9EYc')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Cybernetics')
    btn2 = types.KeyboardButton('Data Science')
    btn3 = types.KeyboardButton('Python')
    btn4 = types.KeyboardButton('MySQL')
    markup.add(btn1, btn2, btn3, btn4)
    welcome_mess = f"Привет, {message.from_user.username}!"
    bot.send_message(message.chat.id, welcome_mess, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == 'cybernetics':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton('1')
        btn2 = types.KeyboardButton('2')
        btn3 = types.KeyboardButton('3')
        btn4 = types.KeyboardButton('4')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = 'Chose your number'

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        btn1 = types.KeyboardButton('Cybernetics')
        btn2 = types.KeyboardButton('Data Science')
        btn3 = types.KeyboardButton('Python')
        btn4 = types.KeyboardButton('MySQL')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = 'Miss your data'

    bot.send_message(message.chat.id, final_message)


@bot.message_handler(content_types=['sticker'])
def sticker(message):
    bot.reply_to(message, "This is fuc**g sticker, bitch!")


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, "Don't send me you dick pic, bitch!")


bot.polling(none_stop=True)
