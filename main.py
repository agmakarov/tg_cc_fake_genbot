import environs
import faker
from telebot import TeleBot, types
from faker import Faker

env = environs.Env()
env.read_env('.env')
BOT_TOKEN = env('BOT_TOKEN')

bot = TeleBot(token=BOT_TOKEN)
fake = Faker()

btn1 = types.KeyboardButton(text='VISA')
btn2 = types.KeyboardButton(text='Mastercard')
btn3 = types.KeyboardButton(text='AMEX')
btn4 = types.KeyboardButton(text='JCB')
markup = types.ReplyKeyboardMarkup(resize_keyboard=True).row(btn1, btn2).row(btn3, btn4)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "💳 Привет, {0.first_name}! Я бот для генерации тестовых карт".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def button_handler(message):
    if(message.text == 'VISA'):
        card_type = 'visa'
    elif(message.text == 'Mastercard'):
        card_type = 'mastercard'
    elif(message.text == 'AMEX'):
        card_type = 'amex'
    elif(message.text == 'JCB'):
        card_type = 'jcb'
    else:
        bot.send_message(message.chat.id, "😔 К сожалению я не умею генерировать карты такого типа, выбери из предложенных вариантов ⬇️", reply_markup=markup)
        return
    
    generated_card = fake.credit_card_full(card_type)
    bot.send_message(message.chat.id, f'Твоя карта 💳:\n{generated_card}')

bot.polling(none_stop=True)