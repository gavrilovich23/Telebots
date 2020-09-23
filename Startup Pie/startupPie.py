import logging
from telegram.ext import (Updater, CommandHandler)


def start(update):
    update.message.reply_text('Hi! I am Startup Pie Bot. '
                              'I would help you to define shares between founders')


def main():
    updater = Updater('1205687194:AAFmQwRrNedfaHRv1G3o5CX2dKSsVCNqqUk', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
