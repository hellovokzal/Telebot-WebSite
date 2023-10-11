python
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
    # Отправка HTML файла через ссылку
    html_url = message.chat.id[6:len(message.chat.id)]
    html_response = requests.get(html_url)

    if html_response.status_code == 200:
        # Установка типа контента и отправка файла пользователю
        bot.send_chat_action(message.chat.id, 'upload_document')
        bot.send_document(message.chat.id, html_response.content)
    else:
        bot.reply_to(message, 'Не удалось загрузить HTML файл.')

# Запуск бота
bot.polling()
