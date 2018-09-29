#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import RU
import tools
import adder
from sqlite3 import Error
from SQLite import SQLite
from telegram import ReplyKeyboardMarkup,ReplyMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(bot, update):
    user = update.message.from_user
    keybrd = [[RU.addolaybut,RU.adddaybut], [RU.reportbut]]
    update.message.reply_text(RU.start, reply_markup=ReplyKeyboardMarkup(keybrd,True))


def help(bot, update):
    update.message.reply_text(RU.help)


def error(bot, update, error):
    tools.log('Update {} caused error {}'.format(update, error), False)

def main():
    updater = Updater(RU.token)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(adder.addoutlayhandler())
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

