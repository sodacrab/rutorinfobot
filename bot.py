# -*- coding: utf-8 -*-

import rutor
from uuid import uuid4
from telegram import ParseMode
from telegram import InlineQueryResultArticle
from telegram import InputTextMessageContent
from telegram.ext import Updater
from telegram.ext import InlineQueryHandler
from telegram.ext import CommandHandler

TOKEN   = '116070187:AAE92oYWPF6H4L62L1V1uJGGL8o-83WknDg'
TITLE   = 'Сиды: %d | Личи: %d'
MESSAGE = '*%s*\n\n`%s`\n\n[Download torrent](%s)'

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Yo')

def handler(bot, update):
    query = update.inline_query.query.strip()
    if query:
        results = list()
        for item in rutor.search(query)[:50]:
            results.append(InlineQueryResultArticle(
                id=uuid4(),
                title=TITLE % (item['seed'], item['leech']),
                description=item['title'],
                input_message_content=InputTextMessageContent(
                    MESSAGE % (item['title'], item['magnet'], item['torrent']),
                    parse_mode=ParseMode.MARKDOWN
                )
            ))
        bot.answerInlineQuery(update.inline_query.id, results)

if __name__ == '__main__':
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(InlineQueryHandler(handler))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()