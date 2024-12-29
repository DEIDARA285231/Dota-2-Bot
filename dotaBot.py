import os
import telebot
import sys
import json
import requests

print(sys.prefix)

#BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_TOKEN = "6312353029:AAFzx4QatmgAcKlCUiiNSOvkU8Qtc000lUY"

bot = telebot.TeleBot(BOT_TOKEN)

file_path = "heroStats.json" 

with open(file_path, "r") as file:
    data = json.load(file)

hero_dict = {hero["localized_name"]: hero["id"] for hero in data}

#print(hero_dict)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hey, nice to meet you, how may I assist you?")

#@bot.message_handler(commands=["Abaddon"])
#def reply(message):
#    headers = {"Content-Type": "application/json; charset=utf-8"}
#    output = requests.get("https://api.opendota.com/api/heroStats",headers=headers, timeout=None)
#    for hero in data:
#        if hero["localized_name"] == "Abaddon":           
#    bot.reply_to(message, )

# Message handler for hero stats
@bot.message_handler(commands=['hero-stats'])
def sign_handler(message):
    text = "What hero are you interested in?\nType its name like this: *Anti-Mage*, *Crystal Maiden*, etc."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_hero)

def fetch_hero(message):
    selected_hero = message.text
    print("SELECTED HERO: " + selected_hero)

    headers = {"Content-Type": "application/json; charset=utf-8"}
    output = requests.get("https://api.opendota.com/api/heroStats",headers=headers, timeout=None)
    data = json.loads(output.content)

    for hero in data:
        print(hero)
        if hero["localized_name"] == selected_hero:
            hero_message = f'*Hero:* {hero["localized_name"]}\\n*Sign:* {sign}\\n*Day:* {data["date"]}'
            bot.send_message(message.chat.id, "Here are the requested stats!")
            bot.send_message(message.chat.id, hero_message, parse_mode="Markdown")

bot.infinity_polling()