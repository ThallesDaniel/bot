import telebot

bot = telebot.TeleBot("suachavevem aqui")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "AIIIIIIIIIIIIIIIIIIIIN ZE DA MANGA")  

@bot.message_handler(commands=['oi'])
def oi(message):
    bot.send_message(message.chat.id, "OI")

@bot.message_handler()
def default(message):
    bot.send_message(message.chat.id, "Não entendi o que você quer dizer.")

bot.polling()