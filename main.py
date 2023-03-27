import telebot
import openai
import os

from config import api, telegram_token


# Получите ключ OpenAI API из своего аккаунта OpenAI
openai.api_key = api

# Инициализируем бота
bot = telebot.TeleBot(telegram_token)


# Определяем функцию, которая будет вызываться при получении сообщения
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получаем текст сообщения от пользователя
    user_input = message.text

    # Обращаемся к API ChatGPT для получения ответа на вопрос пользователя
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}])

    # Получаем ответ от API ChatGPT
    bot_response = response.choices[0].message.content.strip()

    # Отправляем ответ пользователю
    bot.send_message(message.chat.id, bot_response)


# Запускаем бота
bot.polling()
