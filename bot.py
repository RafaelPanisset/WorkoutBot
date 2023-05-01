import telebot
from telebot import types
import random
from exercises import exercises_dict

BOT_TOKEN = 'YOUR_BOT_TOKEN'

bot = telebot.TeleBot(BOT_TOKEN)

# Handles the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the workout bot! To get started, enter /help.")

# Handles the /help command and displays a keyboard with body part options
@bot.message_handler(commands=['help'])
def show_body_parts(message):
    # create keyboard with body part options
    markup = types.ReplyKeyboardMarkup()
    markup.row('Chest', 'Back')
    markup.row('Arms', 'Abdominals')
    markup.row('Legs', 'Shoulders')

    # send message with keyboard
    bot.send_message(message.chat.id, "Select a body part to work on:", reply_markup=markup)

# Handles all other messages and selects exercises based on user input
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == 'Chest':
        exercises = select_exercises('Chest')
        send_exercises(exercises, message.chat.id)
    elif message.text == 'Back':
        exercises = select_exercises('Back')
        send_exercises(exercises, message.chat.id)
    elif message.text == 'Arms':
        exercises = select_exercises('Arms')
        send_exercises(exercises, message.chat.id)
    elif message.text == 'Abdominals':
        exercises = select_exercises('Abdominals')
        send_exercises(exercises, message.chat.id)
    elif message.text == 'Legs':
        exercises = select_exercises('Legs')
        send_exercises(exercises, message.chat.id)
    elif message.text == 'Shoulders':
        exercises = select_exercises('Shoulders')
        send_exercises(exercises, message.chat.id)

# Selects four random exercises from the given body part's exercise list
def select_exercises(body_part):
    exercise_list = exercises_dict.get(body_part.lower())
    return random.sample(list(exercise_list), 4)

# Sends the selected exercises to the user with the specified chat_id
def send_exercises(exercises, chat_id):
    bot.send_message(chat_id, "<b> Here are your workout exercises:</b>", parse_mode='HTML')
    for exercise in exercises:
        name = exercise['name']
        sets = exercise['sets']
        reps = exercise['reps']
        details = exercise['details']
        message = ''
        message += f"<b>{name} ({sets} sets x {reps} reps)</b>\n"
        message += f"<b>Details:</b><i>{details}</i>\n\n"
        bot.send_message(chat_id, message, parse_mode='HTML')

# Start the bot and keep it running indefinitely
bot.infinity_polling()
