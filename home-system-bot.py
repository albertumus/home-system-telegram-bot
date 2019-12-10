# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:59:48 2019

@author: admin
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import telegram
from apscheduler.schedulers.background import BackgroundScheduler



sched = BackgroundScheduler()

def one_hour_tasks(bot):
    bot.send_message(chat_id=-357831632, text="¡Cuidado la temperatura de casa ha bajado de 3 grados!")

def ten_seconds_tasks(bot):
    bot.send_message(chat_id=-357831632, text="Este es un mensaje que se repite cada 10 segundos")


    
def saludo(bot, update):
    username = update.effective_user.username
    msg = "Saludos, {}".format(username)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=msg)

def temperatura(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="La temperatura es de 10 grados pollitales") 

def unknown(bot, update):
    chat_id = update.message.chat_id
    print(chat_id)
    bot.send_message(chat_id=chat_id, text="Lo siento. No reconozco ese mensaje")
    
def registry_commands(dp):
    dp.add_handler(CommandHandler('saludo',saludo))
    dp.add_handler(CommandHandler('frase',frase_ñaña)) 
    dp.add_handler(CommandHandler('temp', temperatura))
    # Controlador de Comandos No Creados
    dp.add_handler(MessageHandler(Filters.command, unknown))

def main():
    bot = telegram.Bot(token='')
    updater = Updater('')
    
    sched.add_job(ten_seconds_tasks, 'interval', args=[bot], seconds=10)
    sched.add_job(one_hour_tasks, 'interval', args=[bot],seconds=3600)
    sched.start()
    
    dp = updater.dispatcher  
    registry_commands(dp)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

sched.pause()
