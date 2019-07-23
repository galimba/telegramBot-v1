#!/usr/bin/env python3
from telegram.ext import Updater, CommandHandler
import datetime
import sys
import os
import random

targetDate= datetime.datetime(2019,9,6) # Julian's birthday!
all_facts={}

def getCountdown():
    diff= (targetDate - datetime.datetime.today()).days
    return(diff)

def countdown(bot, update):
    print('getCountdown')
    rand_fact_id= random.randint(0,len(all_facts))
    update.message.reply_text("We are {} days away!! Here is a random fact to pass the time... {} {} ".format(getCountdown(),"\n\n\n", all_facts[rand_fact_id]))

def fact(bot, update):
    print('randomFact')
    rand_fact_id= random.randint(0,len(all_facts))
    update.message.reply_text("Ok, here it goes... {} {} ".format("\n\n", all_facts[rand_fact_id]))

def main():
    print('main - reading fact list')
    filepath = 'facts.lst'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
            all_facts[cnt]=line
    print('main - {} facts read'.format(cnt))
    updater = Updater('____PUT_CREDENTIALS_HERE____')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('countdown',countdown))
    dp.add_handler(CommandHandler('fact',fact))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
