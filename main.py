import telebot
import schedule
import time
from threading import Thread
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

CHAT_ID = None

missoes_diarias = [
    "Missão 05:00 - Ritual da Lâmina: Levante, treine e escreva uma frase estoica.",
    "Missão 14:00 - Ritual do Confronto: Simule um embate com sua Sombra.",
    "Missão 22:00 - Ritual das Sombras: Relate 1 erro, 1 acerto, 1 recalibração."
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    bot.send_message(CHAT_ID, "Bem-vindo, I-7. IsaacBot v2.7 iniciado. Rotina sincronizada.")

def enviar_missoes():
    if CHAT_ID:
        for msg in missoes_diarias:
            bot.send_message(CHAT_ID, msg)

def rotina():
    schedule.every().day.at("05:00").do(lambda: bot.send_message(CHAT_ID, missoes_diarias[0]))
    schedule.every().day.at("14:00").do(lambda: bot.send_message(CHAT_ID, missoes_diarias[1]))
    schedule.every().day.at("22:00").do(lambda: bot.send_message(CHAT_ID, missoes_diarias[2]))
    while True:
        schedule.run_pending()
        time.sleep(30)

def start_bot():
    Thread(target=rotina).start()
    bot.polling()

start_bot()
