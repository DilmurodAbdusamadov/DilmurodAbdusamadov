import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


user_opt = dict()
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level=logging.INFO)

def start(update, context):
    user = update.message.from_user
    user_opt[user.id] = None
    buttons = [
        [
            InlineKeyboardButton('Check', callback_data='1'),
            InlineKeyboardButton('Contacts', callback_data='2'),
        ]
    ]
    update.message.reply_text('<i>Welcome <b>{},</b>\n \n<b>Compose bold, clear, mistake-free writing with '
                              'Grammist. Elevate your writing to the next level!</b></i>\n\n'.format(user.first_name),
                              reply_markup=InlineKeyboardMarkup(buttons),
                              parse_mode='html')


def handle_message(update, context):
    text = str(update.message.text)
    logging.info(f'User ({update.message.chat.id}) says: {text}')
    correct_text = TextBlob(text).correct()
    emotion_text = TextBlob(text, analyzer=NaiveBayesAnalyzer()).sentiment
    if emotion_text[1] > emotion_text[2]:
        update.message.reply_text(f'<i>{correct_text}\n\n<b>Your text sounds positive.😊</b></i>', parse_mode='html')
    elif emotion_text[1] < emotion_text[2]:
        update.message.reply_text(f'<i>{correct_text}\n\n<b>Your text sounds negative.😡</b></i>', parse_mode='html')


def inline_callback(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    user_opt[user_id] = int(query.data)
    query.message.reply_text(text='<i><b>To err is human; to edit divine.</b>\n\nEnter your text below, '
                                  'please👇</i>', parse_mode='html')


def main():
    updater = Updater('5432145872:AAF0zmug-y-qPJP62vGsipvQthSxyWjjtbI', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(inline_callback))
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    updater.start_polling()
    updater.idle()


main()