from telebot import TeleBot

# Уникальный токе который получаем от @BotFather
TOKEN = '5948006079:AAF91Lwm13HAh34qUT_LAJtNgtSpBZ9QHLI'
bot = TeleBot(TOKEN)

# Бот реагирует на команду /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

# Бот реагирует на любое сообщение, кроме /start
@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
