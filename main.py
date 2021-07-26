import re
import telebot

KEYS = {'ира', 'иры', 'ире', 'иру', 'ирой', 'ирина', 'ирины', 'ирине', 'ирину', 'ириной', 'ирка', 'ирочка', 'ириска', 'ирусик', 'ириночка', 'ирунидзе', 'иридзе', 'сыр'}
BOT_TOKEN = "1835508336:AAFT0olkFzHR70sRQKo6h9P3CEYrArgw1tw"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  words = set(re.findall(r'\w+', message.text.lower()))
  if (KEYS & words):
    bot.send_message(message.chat.id, 'Да кто такая эта ваша Ира?')
      
bot.polling()