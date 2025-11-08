import telebot, random
token = '8515233393:AAFKYZCySQClNeGmALS1ookCl69fNJ9MO9E'
bot = telebot.TeleBot(token)

random_rus_town = [
    "Биробиджан",
    "Птичник",
    "Аэропорт",
    "Валдгеймское",
    "Кирга",
    "Найфельд",
    "Известковое",
    "Теплоозерское",
    "Дипкунский",
    "Бердигестях",
    "Новоангарск",
    "Тарко-Сале",
    "Тимшер",
    "Вологда",
    "Дмитровград",
    "Сорочинск",
    "Благовещенск",
    "Кармаскалы",
    "Красноусольский",
    "Армизонское"


]

@bot.message_handler(commands=['start']) # /start
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот-помощник')

@bot.message_handler(commands=['random_russian_town'])
def random_russian_town(message):
    bot.send_message(message.chat.id, random.choice(random_rus_town))

bot.polling()