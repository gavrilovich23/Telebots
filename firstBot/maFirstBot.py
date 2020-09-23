import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(token='1393828282:AAEx8Cpy9GhNxVmQgsU9BP2gKjpX4cURhrE', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Woot-woopety-woot! I am a bot that help you too '
                                                                    'be more productive')


def fuck(update, context):
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('src/fuck_you_all.wav', 'rb'))


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

fuck_handler = CommandHandler('stop', fuck)
dispatcher.add_handler(fuck_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


print('Bot has been launched')
updater.start_polling()
