#!/usr/bin/env python3
from telegram.ext import Updater, CommandHandler
import datetime

targetDate= datetime.datetime(2019,9,6,17,00)

def getCountdown():
    diff= (targetDate - datetime.datetime.today()).days
    return(diff)

def countdown(bot, update):
    print('getCountdown')
    update.message.reply_text('We are {} days away!!'.format(getCountdown()))


def main():
    print('main')
    updater = Updater('BOT-CREDENTIALS-GO-HERE')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('countdown',countdown)) #bot will reply to /countdown command
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
