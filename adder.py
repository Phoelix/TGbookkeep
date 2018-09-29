#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import RU
import re
import tools
from SQLite import SQLite
from sqlite3 import Error
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, RegexHandler, \
    Filters
from telegram import ReplyKeyboardMarkup, ReplyMarkup

MSG, DAY = range(2)

def addoutlayhandler():
    handler = ConversationHandler(
    entry_points=[RegexHandler(RU.addolaybut, intro)],
        states={
            MSG: [RegexHandler('END', end),
                  MessageHandler(Filters.all, adding)]
        },
        fallbacks=[RegexHandler('END', end)])
    return handler


def adddayhandler():
    handler = ConversationHandler(
    entry_points=[RegexHandler(RU.adddaybut, dayintro)],
        states={
            MSG: [RegexHandler('END', end),
                  MessageHandler(Filters.all, dayadding)]
        },
        fallbacks=[RegexHandler('END', end)])
    return handler


def intro(bot, update):
    keybrd = [['END']]
    db = SQLite()
    text = RU.addolay
    otypes = db.magic('select id, name from otype').fetchall()
    for i in otypes:
        text += '{} {}\n'.format(i[0], i[1])
    update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(keybrd,True))
    return MSG

def adding(bot, update):
    db = SQLite()
    text = update.message.text[2:]
    oval = re.search(r'^\d+', text).group(0)
    otype = update.message.text[:2]
    text = text.replace(oval,'')
    date = tools.getdate()
    res = db.magic('insert into outlay(type, value, date, text) VALUES (?,?,?,?)', (otype, oval, date, text)).fetchall()
    update.message.reply_text('Done')
    return MSG

def end(bot, update):
    keybrd = [[RU.addolaybut, RU.adddaybut], [RU.reportbut]]
    update.message.reply_text(RU.start, reply_markup=ReplyKeyboardMarkup(keybrd, True))
    return ConversationHandler.END


def dayintro(bot, update):
    keybrd = [['END']]
    update.message.reply_text(RU.addday, reply_markup=ReplyKeyboardMarkup(keybrd, True))
    return MSG

def dayadding(bot, update):
    db = SQLite()
    text = update.message.text
    date = tools.getdate()
    try: res = db.magic('insert into alday(date,val) values (?,?)', (date, text))
    except Error as e: update.message.reply_text('ERROR ADDING'+ str(e))
    return MSG