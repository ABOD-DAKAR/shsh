import telebot , random , requests
from telebot import types
bot = telebot.TeleBot(input("EnTeR YoU ToKeN : "))
o8  = types.InlineKeyboardButton(text = "غنيلي", callback_data = 'ok')
o98  = types.InlineKeyboardButton(text = "مره اخرئ 🔄", callback_data = 'ok9')
@bot.callback_query_handler(func=lambda call: True)
def ButOn(call):
 if call.data =="ok":
  voic(call.message)
 if call.data =="ok9":
  voic(call.message)
@bot.message_handler(commands=['start'])
def start(message):
 msg4 = types.InlineKeyboardMarkup(row_width=1)
 msg4.add(o8)
 bot.reply_to(message,text="""اهلاً بك عزيزي 👋🏻
في بوت غنيلي ❤️‍🔥
ارسل ( غنيلي ) او اختر من الاسفل 👤""",reply_markup=msg4)
@bot.message_handler(func=lambda m:True)   
def get(message):
     msg = message.text
     if msg == "غنيلي":
      s = random.randint(8,271)
      k = int(s)
      o = f"https://t.me/DAKAR130/{k}"
      msg4 = types.InlineKeyboardMarkup(row_width=1)
      msg4.add(o98)
      bot.send_voice(message.chat.id,o,reply_markup=msg4)
def voic(message):
 s = random.randint(8,271)
 k = int(s)
 o = f"https://t.me/DAKAR130/{k}"
 msg4 = types.InlineKeyboardMarkup(row_width=1)
 msg4.add(o98)
 bot.send_voice(message.chat.id,o,reply_markup=msg4)
bot.polling(none_stop=True)