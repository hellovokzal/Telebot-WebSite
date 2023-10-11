
import telebot
import requests

# Вставьте ваш токен для доступа к API телеграм-бота
TOKEN = '6657397651:AAH_4FBmSWUE-wPnSgskKzIi8wUjd4PGi2M'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введите команду /send")

@bot.message_handler(commands=['send'])
def send(message):
    try:
        text = str(message.text)[6:]
        url = requests.get(text)
        with open("index.html", "w") as file1:
                file1.write(url.text)
                # Отправка файла index.html
        with open('index.html', 'rb') as file:
                bot.send_chat_action(message.chat.id, 'upload_document')
                bot.send_document(message.chat.id, file)

    except:
        bot.reply_to(message, 'Ошибка ссылки!')

# Запуск бота
bot.polling()
