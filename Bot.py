import telebot
import requests
from bs4 import BeautifulSoup


def get_htmlanek(url, params=None):
	ranek = requests.get(url, headers=headersanek, params=params)
	ranek.encoding = 'utf-8'
	return ranek


def get_contentanek(html):
	soupanek = BeautifulSoup(html, 'html.parser')
	itemsanek = soupanek.find('div', class_='text').get_text()
	return itemsanek

def get_html(url, params=None):
    r = requests.get(url, headers=headers1, params=params)
    r.encoding = 'utf-8'
    return r
def parseanek():
	htmlanek = get_htmlanek(urlanek)
	if htmlanek.status_code == 200:
		return get_contentanek(htmlanek.text)

	else:
		Print('Error')


def get_weather(city):
	req = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=8915429fcf6a68275f7c20caab444827&units=metric&lang=RU"
	res = requests.get(req)
	data = res.json()
	try:
		answer = "В городе " + data['name'] + " сейчас " + str(data['main']['temp']) + " °С и " + data['weather'][0]['description']
	except:
		return "Дідько! Такого міста не існує, здається("
	return answer
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('span').get_text()
    return items


def parse():
    html = get_html(url1)
    if html.status_code == 200:
        return get_content(html.text)
        
    else:
        Print('Error')

bot = telebot.TeleBot('1287225917:AAE2H4WbxZPaSlFb2G7doWx9r43kGzajxqo')


urlanek = 'https://www.anekdot.ru/random/anekdot/'
headersanek = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0', 'accept': '*/*'}
url1 = 'http://kakoysegodnyaprazdnik.ru/'
headers1 = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
            'accept': '*/*'}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	textt = message.text
	textt = textt.split()
	if textt[0] == "Погода":
		bot.send_message(message.chat.id, get_weather(textt[1]))					
	if message.text == "Блять":
		bot.send_message(message.chat.id, "Не матерись")
	if message.text == "Степа":
		bot.send_message(message.chat.id, "Он лох")
	if message.text == "блять":
		bot.send_message(message.chat.id, "Не матерись")
	if message.text == "пиздец":
		bot.send_message(message.chat.id, "Не матерись")
	if message.text == "Пиздец":
		bot.send_message(message.chat.id, "Не матерись")
	if message.text == "Сука":
		bot.send_message(message.chat.id, "Не мат, но все равно неприятно :(")
	if message.text == "Слава Україні!":
		bot.send_message(message.chat.id, "Героям слава!")
	if message.text == "Слава Україні":
		bot.send_message(message.chat.id, "Где эмоции???")
	if message.text == "Слава нації!":
		bot.send_message(message.chat.id, "Смерть ворогам!")
	if message.text == "Слава нації":
		bot.send_message(message.chat.id, "Где эмоции???")
	if message.text == "Україна!":
		bot.send_message(message.chat.id, "Понад усе!")
	if message.text == "Путін":
		bot.send_message(message.chat.id, "Хуйло")
	if message.text == "Путин":
		bot.send_message(message.chat.id, "Хуйло")
	if message.text == "Пидор":
		bot.send_message(message.chat.id, "Ты")
	if message.text == "Юра":
		bot.send_message(message.chat.id, "Клоун")
	if message.text == "Настя":
		bot.send_message(message.chat.id, "Жопа")
	if message.text == "Женя":
		bot.send_message(message.chat.id, "Токс")
	if message.text == "Артем":
		bot.send_message(message.chat.id, "Сишник")
	if message.text == "Сеня":
		bot.send_message(message.chat.id, "Бухххалтер")
	if message.text == "Дима":
		bot.send_message(message.chat.id, "Кокосик")
	if message.text == "Спокойной ночи":
		bot.send_message(message.chat.id, "Спокойной)")
	if message.text == "Привет":
		bot.send_message(message.chat.id, "Привет, солнце!")
	if message.text == "Праздник":
		day = parse()
		bot.send_message(message.chat.id, "Сегодня " + day)
	if message.text == "Анекдот":
		anek = parseanek()
		bot.send_message(message.chat.id, anek)
	if message.text == "Юра!":
		bot.send_message(message.chat.id, "@Chipperio")
	if message.text == "Абоба":
		bot.send_message(message.chat.id, "Aboba)")
	if message.text == "Настя!":
		bot.send_message(message.chat.id, "@agent_sever")
	if message.text == "Женя!":
		bot.send_message(message.chat.id, 'Могу просто покричать: "ЖЕНЯЯ!!!!"')
	if message.text == "Георг, а ты пойдешь?":
		bot.send_message(message.chat.id, 'Да, конечно, го')
	if message.text == "Тема!":
		bot.send_message(message.chat.id, '@where_my_wings')
	if message.text == "Сеня!":
		bot.send_message(message.chat.id, 'Могу просто покричать: "АРСЕНИЙ!!!!"')
	if message.text == "Дима!":
		bot.send_message(message.chat.id, "@dimakovua")
	if message.text == "@dimakovua":
		bot.send_message(message.chat.id, 'Он уже летит. Я верю <3')
	if message.text == "Доброе утро":
		day = parse()
		anek = parseanek()
		bot.send_message(message.chat.id, "Доброе утро, господа! Сегодня " + day + "! Желаю вам успешно провести ваши последние (что весьма вероятно) дни существования достойно)))")
		bot.send_message(message.chat.id, "Анекдот сегодняшнего дня: "+anek)
	
    

bot.polling(none_stop=True, interval=0)
