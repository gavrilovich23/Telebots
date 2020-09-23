import telebot

bot = telebot.TeleBot('1010193101:AAGmwWvcWNEKU_q1VuD5vApJo00LfrYfScc')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "* Oh, hello!*\nHow are you doing, *bitch*!?", parse_mode='Markdown')


@bot.message_handler(content_types=['sticker'])
def ans_sticker(message):
    bot.reply_to(message, "Don't use this fucking stickers, *bitch*", parse_mode='markdown')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text + ', bitch!')


bot.polling()
