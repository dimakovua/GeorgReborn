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
		print("We are")
		print(get_weather(textt[1]))
		bot.reply_to(message, get_weather(textt[1]))
	if message.text == "Георг лох":
		bot.reply_to(message, "Пипец вам")
		c = 1
		while c < 10:
			bot.reply_to(message, "Пипец вам")
			bot.reply_to(message, "Я предупреждал!")
			bot.reply_to(message, "Я же не тупой бот")
			bot.reply_to(message, "Ща еще будем тэгать")
			bot.reply_to(message, "@dimakovua")
			bot.reply_to(message, "@agent_sever")
			anek = parseanek()
			bot.reply_to(message, anek)
			c = c + 1
			
		
	if message.text == "Блять":
		bot.reply_to(message, "Не матерись")
	if message.text == "Степа":
		bot.reply_to(message, "Он лох")
	if message.text == "блять":
		bot.reply_to(message, "Не матерись")
	if message.text == "пиздец":
		bot.reply_to(message, "Не матерись")
	if message.text == "Пиздец":
		bot.reply_to(message, "Не матерись")
	if message.text == "Сука":
		bot.reply_to(message, "Не мат, но все равно неприятно :(")
	if message.text == "Слава Україні!":
		bot.reply_to(message, "Героям слава!")
	if message.text == "Слава Україні":
		bot.reply_to(message, "Где эмоции???")
	if message.text == "Слава нації!":
		bot.reply_to(message, "Смерть ворогам!")
	if message.text == "Слава нації":
		bot.reply_to(message, "Где эмоции???")
	if message.text == "Україна!":
		bot.reply_to(message, "Понад усе!")
	if message.text == "Путін":
		bot.reply_to(message, "Хуйло")
	if message.text == "Путин":
		bot.reply_to(message, "Хуйло")
	if message.text == "Пидор":
		bot.reply_to(message, "Ты")
	if message.text == "Юра":
		bot.reply_to(message, "Клоун")
	if message.text == "Настя":
		bot.reply_to(message, "Жопа")
	if message.text == "Женя":
		bot.reply_to(message, "Токс")
	if message.text == "Артем":
		bot.reply_to(message, "Сишник")
	if message.text == "Сеня":
		bot.reply_to(message, "Бухххалтер")
	if message.text == "Дима":
		bot.reply_to(message, "Кокосик")
	if message.text == "Спокойной ночи":
		bot.reply_to(message, "Спокойной)")
	if message.text == "Привет":
		bot.reply_to(message, "Привет, солнце!")
	if message.text == "Праздник":
		day = parse()
		bot.reply_to(message, "Сегодня " + day)
	if message.text == "Анекдот":
		anek = parseanek()
		bot.reply_to(message, anek)
	if message.text == "Юра!":
		bot.reply_to(message, "@Chipperio")
	if message.text == "Абоба":
		bot.reply_to(message, "Aboba)")
	if message.text == "Настя!":
		bot.reply_to(message, "@agent_sever")
	if message.text == "Женя!":
		bot.reply_to(message, 'Могу просто покричать: "ЖЕНЯЯ!!!!"')
	if message.text == "Георг, а ты пойдешь?":
		bot.reply_to(message, 'Да, конечно, го')
	if message.text == "Тема!":
		bot.reply_to(message, '@where_my_wings')
	if message.text == "Сеня!":
		bot.reply_to(message, 'Могу просто покричать: "АРСЕНИЙ!!!!"')
	if message.text == "Дима!":
		bot.reply_to(message, "@dimakovua")
	if message.text == "@dimakovua":
		bot.reply_to(message, 'Он уже летит. Я верю <3')
	if message.text == "Доброе утро":
		day = parse()
		anek = parseanek()
		bot.reply_to(message, "Доброе утро, господа! Сегодня " + day + "! Желаю вам успешно провести ваши последние (что весьма вероятно) дни существования достойно)))")
		bot.reply_to(message, "Анекдот сегодняшнего дня: "+anek)
	
    

bot.polling(none_stop=True, interval=0)
