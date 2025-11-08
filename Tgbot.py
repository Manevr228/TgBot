import telebot
token = '8515233393:AAFKYZCySQClNeGmALS1ookCl69fNJ9MO9E'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start']) # /start
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот-помощникц')

bot.polling()