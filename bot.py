from telegram import *
from telegram.ext import *

TOKEN = ""
MY_ID = ""

def start(update, context):
	try:
		update.message.reply_text(f"""Hola<a href="tg://user?id={update.message.from_user.id}"> {update.message.from_user.first_name}</a>.
Bienvenido a FeedBBot. 

¿Que es FeedBBot?
- FeedBBot es un bot de Feedback creado por @hw_dev

¿Para que sirve?
- Sirve para obtener comentarios sobre lo que el dueño realize. Por ejemplo: Dibujar, Cantar o programar.

¿Puedo obtener una copia de FeedBBot?
- Claro que sí. FeedBBot es un bot de código abierto. Cualquiera puede obtener una copia y modificarlo. """, parse_mode="HTML",reply_markup=InlineKeyboardMarkup([
[InlineKeyboardButton(text='Canal del desarrollador👥', url='t.me/hw_dev')],
            ]))
	except:
		update.message.reply_text("Por favor configure su nombre de usuario para usar el bot")
		
def filtro(update, context):
	text = update.message.text
	if "/start" == text:
		pass
	else:
		context.bot.sendMessage(chat_id=MY_ID, text=text)
	
updater = Updater(TOKEN)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
#=====#
dp.add_handler(MessageHandler(Filters.text, filtro))
#=====#

print("online")
updater.start_polling(allowed_updates=Update.ALL_TYPES)
updater.idle()
 
