import telebot
bot = telebot.TeleBot('1604047228:AAF6L-8hNLABgiEaomjBtokHKWFv1LAbPdY')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
         bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'погода':
        bot.send_message(message.from_user.id, 'погода сегодня хорошая')
    else:
        bot.send_message(message.from_user.id, 'Все будет хорошо, {0}'.format(message.from_user.first_name))
bot.polling(none_stop=True)
