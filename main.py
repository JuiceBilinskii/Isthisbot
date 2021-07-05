import re
import telebot

KEYS = {'ира', 'иры', 'ире', 'иру', 'ирой', 'ирина', 'ирины', 'ирине', 'ирину', 'ириной'}
BOT_TOKEN = "1835508336:AAFT0olkFzHR70sRQKo6h9P3CEYrArgw1tw"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  words = set(re.findall(r'\w+', message.text.lower()))
  if (KEYS & words):
    bot.reply_to(message, 'Это та, кто вонюче срет?')
      
bot.polling()