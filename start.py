import telebot
import requests

# Вставьте ваш токен для доступа к API телеграм-бота
TOKEN = '6657397651:AAH_4FBmSWUE-wPnSgskKzIi8wUjd4PGi2M'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введите команду /send")

@bot.message_handler(func=lambda message: True)
def echo(message):
    text1 = str(message.text)[0:8]
    text2 = str(message.text)[0:7]
    if text1 == "https://" or text2 == "http://":
        try:
            text = str(message.text)
            url = requests.get(text)
            with open("index.html", "w") as file1:
                    file1.write(url.text)
                    # Отправка файла index.html
            with open('index.html', 'rb') as file:
                    bot.send_chat_action(message.chat.id, 'upload_document')
                    bot.send_document(message.chat.id, file)

        except:
            bot.reply_to(message, 'Ошибка ссылки!')
    else:
        bot.send_message(message.chat.id, "Неверная ссылка!")
        

# Запуск бота
bot.polling()
