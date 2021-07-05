import os
import re
import telebot

KEYS = {'ира', 'иры', 'ире', 'иру', 'ирой', 'ирина', 'ирины', 'ирине', 'ирину', 'ириной'}
BOT_TOKEN = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(BOT_TOKEN)

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, '123')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  words = set(re.findall(r'\w+', message.text.lower()))
  if (KEYS & words):
    bot.send_message(message.from_user.id, 'Это та, кто вонюче срет?')
      
bot.polling()