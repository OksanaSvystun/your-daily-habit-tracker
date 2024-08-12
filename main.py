    #"6845655438:AAEN_0uwzga7BSXsMe9D7F7DnKQEb0IpAt4"


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, CallbackContext, MessageHandler, filters

# Задаємо повідомлення українською
messages = {
    'welcome': 'Слава Україні!',
    'menu': 'Виберіть дію:',
    'new_habbit': 'Напишіть назву звички:',
    'delete_habit': 'Оберіть звичку, яку потрібно видалити:',
    'track_habbit': 'Оберіть звичку:',
    'see_progress': 'Посилання на прогрес:'
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(messages['welcome'])

    keyboard = [
        [InlineKeyboardButton("Додати нову звичку", callback_data='button_add_habit')],
        [InlineKeyboardButton("Відмітити виконання звички", callback_data='button_track_habit')],
        [InlineKeyboardButton("Перестати відслідковувати звичку", callback_data='button_stop_habit')],
        [InlineKeyboardButton("Переглянути мій прогрес", callback_data='button_see_progress')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(messages['menu'], reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'button_add_habit':
        await query.message.reply_text(text=messages['new_habbit'])
    elif query.data == 'button_track_habit':
        await query.message.reply_text(text=messages['track_habbit'])
    elif query.data == 'button_stop_habit':
        await query.message.reply_text(text=messages['delete_habit'])
    elif query.data == 'button_see_progress':
        await query.message.reply_text(text=messages['see_progress'])

if __name__ == '__main__':
    app = ApplicationBuilder().token('6845655438:AAEN_0uwzga7BSXsMe9D7F7DnKQEb0IpAt4').build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()
