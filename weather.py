import requests
s_city = "Ryazan,RU"
city_id = 0
appid = "8a52a28bcfaa6c6a23475a814709495f"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("условия:", data['weather'][0]['description'])
    print("температура:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (weather):", e)
    pass

import telebot
bot = telebot.TeleBot('1604047228:AAF6L-8hNLABgiEaomjBtokHKWFv1LAbPdY')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
         bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'погода':
        bot.send_message(message.from_user.id, 'погода сегодня супер, на улице {0}'.format(data['weather'][0]['description']))
        bot.send_message(message.from_user.id, 'температура сейчас, {0}'.format(data['main']['temp']))
        bot.send_message(message.from_user.id, 'температура минимальная, {0}'.format(data['main']['temp_min']))
        bot.send_message(message.from_user.id, 'температура максимальная, {0}'.format(data['main']['temp_max']))
    elif message.text.lower() == 'прогноз':
        bot.send_message(message.from_user.id, 'сообщаю прогноз погоды ')
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            for i in data['list']:
                bot.send_message(message.from_user.id, i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
        except Exception as e:
            print("Exception (forecast):", e)
            pass

    else:
        bot.send_message(message.from_user.id, 'Все будет хорошо, {0}'.format(message.from_user.first_name))
bot.polling(none_stop=True)


try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    for i in data['list']:
        print( i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'] )
except Exception as e:
        print("Exception (forecast):", e)
        pass
