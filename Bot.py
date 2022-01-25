from imghdr import what
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pytube import YouTube
import os
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, message
from config import TOKEN

loger_chat_id = "-792836774"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
users_flags = {12: 12}

weather_flag = 0
video_flag = 0
audio_flag = 0
#Creating main keyboard
button_video = KeyboardButton('Відео 📹')
button_music = KeyboardButton('Музика 🎵')
button_weather = KeyboardButton('Погода ☀️')
main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
main_kb.row(button_video, button_music)
main_kb.add(button_weather)
#Creating aboba keyboard to stop asking link
button_aboba = KeyboardButton('абоба')
aboba_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
aboba_kb.add(button_aboba)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    global loger_chat_id
    await message.reply("Привіт) \nЯ Георг. Намагаюся бути корисним)))))))", reply_markup=main_kb)
    await bot.send_message(loger_chat_id, "Мене хтось запустив!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(text = "☀️Я дізнаюсь для тебе погоду в будь-якому місті за допомогою /weather \n📹 Я можу скачати для тебе коротесенький мєм з Ютубчика. Спробуй /video\n🎵 Я відправлю тобі музику с відео на Ютуб! Трішки піратство, але спробуй /music")

@dp.message_handler(lambda message: message.text == 'Погода ☀️')
@dp.message_handler(commands=['weather'])
async def weather(message: types.Message):
    global loger_chat_id
    global weather_flag
    global users_flags
    arguments = ""
    if(users_flags.get(message.from_user.id) == 1):
        arguments = message.text
    else:
        arguments = message.get_args()
    try:
        print(arguments)
        req = "http://api.openweathermap.org/data/2.5/weather?q=" + arguments + "&appid=8915429fcf6a68275f7c20caab444827&units=metric&lang=UA"
        res = requests.get(req)
        data = res.json()
        answer = "У місті " + arguments + " зараз " + str(data['main']['temp']) + " °С та " + data['weather'][0]['description']
        weather_flag = 0
        users_flags.pop(message.from_user.id)
        await bot.send_message(message.chat.id, text=answer)
        await bot.send_message(message.chat.id, text="Щось ще?)", reply_markup=main_kb)
        await bot.send_message(loger_chat_id, "Хтось дізнався погоду в " + arguments + "!")
    except:
        weather_flag
        weather_flag = 1
        users_flags[message.from_user.id] = 1
        await bot.send_message(message.chat.id, text="Напиши назву міста (або натисни абоба)", reply_markup=aboba_kb)

@dp.message_handler(lambda message: message.text == 'Відео 📹')
@dp.message_handler(commands=['video'])
async def video(message: types.Message):
    global loger_chat_id
    global video_flag
    global users_flags
    print(video_flag)
    arguments = ""
    if(users_flags.get(message.from_user.id) == 2):
        arguments = message.text
        print(arguments)
    else:
        arguments = message.get_args()
    try:
        yt = YouTube(arguments)
    except:
        users_flags[message.from_user.id] = 2
        await bot.send_message(message.chat.id, text="Кинь силку на Ютуб (або натисни абоба)", reply_markup=aboba_kb)
        return
    if(yt.length < 300):
        print(users_flags)
        await bot.send_message(message.chat.id, text="Секундочку..")
        name_of_video = yt.title
        print(name_of_video)
        video = yt.streams.filter(res="360p",).first().download(filename=name_of_video+".mp4")
        print("OK")
        video_to_send = open(name_of_video+".mp4", 'rb')
        await bot.send_video(message.chat.id, video=video_to_send, supports_streaming=True)
        await bot.send_message(message.chat.id, text="Щось ще?)", reply_markup=main_kb)
        os.remove(name_of_video+".mp4")
        await bot.send_message(loger_chat_id, text="Хтось скачав відео\n" + arguments)
        video_flag = 0
        users_flags.pop(message.from_user.id)
    else:
        video_flag = 0
        users_flags.pop(message.from_user.id)
        await bot.send_message(message.chat.id, text="У мене сервера на 600 мб. Мб тобі ще Інтерстеллар скачати?(((((")
@dp.message_handler(lambda message: message.text == 'Музика 🎵')
@dp.message_handler(commands=['music'])
async def audio(message: types.Message):
    global loger_chat_id
    global audio_flag
    global users_flags
    print(audio_flag)
    arguments = ""
    if(users_flags.get(message.from_user.id) == 3):
        arguments = message.text
        print(arguments)
    else:
        arguments = message.get_args()
    try:
        yt = YouTube(arguments)
    except:
        users_flags[message.from_user.id] = 3
        await bot.send_message(message.chat.id, text="Кинь силку на Ютуб (або натисни абоба)", reply_markup=aboba_kb)
        return
    if(yt.length < 300):
        await bot.send_message(message.chat.id, text="Секундочку..")
        name_of_audio = yt.title
        music = yt.streams.filter(only_audio=True).first().download(filename=name_of_audio+".mp3")
        audio_to_send = open(name_of_audio+".mp3", 'rb')
        await bot.send_audio(message.chat.id, audio=audio_to_send)
        await bot.send_message(message.chat.id, text="Щось ще?)", reply_markup=main_kb)
        # await bot.send_video(message.from_user.id, video=video_to_send, supports_streaming=True)
        os.remove(name_of_audio+".mp3")
        await bot.send_message(loger_chat_id, text="Хтось скачав музику\n" + arguments)
        users_flags.pop(message.from_user.id)
    else:
        users_flags.pop(message.from_user.id)
        await bot.send_message(message.chat.id, text="У мене сервера на 600 мб. Мб тобі ще Інтерстеллар скачати?(((((", reply_markup=main_kb)

@dp.message_handler()
async def echo_message(msg: types.Message):
    global weather_flag
    global video_flag
    global audio_flag
    global users_flags
    print(users_flags)
    if(users_flags.get(msg.from_user.id)):
        if(True):
            if(users_flags.get(msg.from_user.id) == 1 and msg.text != "абоба"):
                await weather(message=msg)
                return
            if(users_flags.get(msg.from_user.id) == 2 and msg.text != "абоба"):
                print(")))")
                await video(message=msg)
                return
            if(users_flags.get(msg.from_user.id) == 3 and msg.text != "абоба"):
                await audio(message=msg)
                return
            else:
                await bot.send_message(msg.chat.id, text="Добре)\nВідстану від тебе")
                await bot.send_message(msg.chat.id, text="Щось ще?)", reply_markup=main_kb)
                users_flags.pop(msg.from_user.id)
                return


if __name__ == '__main__':
    print(users_flags)
    bot.send_message(loger_chat_id, text="Я стартанув!")

    executor.start_polling(dp)