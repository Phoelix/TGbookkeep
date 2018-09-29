#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import RU
import re
import tools
import telegramcalendar
from SQLite import SQLite
from sqlite3 import Error
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, RegexHandler, \
    Filters
from telegram import ReplyKeyboardMarkup, ReplyMarkup


MAD, MNTH, DATE= range(3)
fdate, ldate = range(2)

def rephandler():
    olayhndlr = ConversationHandler(
        entry_points=[RegexHandler(RU.reportbut, intro)],
        states={
            MNTH:[],
            DATE:[]
        },
    fallbacks=[CommandHandler('cancel', end)])

    daytradehndlr = ConversationHandler(
        entry_points=[RegexHandler(RU.reportbut, intro)],
        states={
            MNTH:[],
            DATE:[]
        },
    fallbacks=[CommandHandler('cancel', end)])

    handlr= ConversationHandler(
        entry_points=[RegexHandler(RU.reportbut, intro)],
        states={
            MAD:[]
        },

    fallbacks = [CommandHandler('cancel', end)])

def calendar_handler(bot,update):
    update.message.reply_text("Please select a date: ",
                        reply_markup=telegramcalendar.create_calendar())


def intro(bot, update):
    db = SQLite()
    global f
    update.message.reply_text("Please select a date: ",
                        reply_markup=telegramcalendar.create_calendar())
    return DATE

def end(bot, update):
    keybrd = [[RU.addolaybut, RU.adddaybut], [RU.reportbut]]
    update.message.reply_text(RU.start, reply_markup=ReplyKeyboardMarkup(keybrd, True))
    return ConversationHandler.END
