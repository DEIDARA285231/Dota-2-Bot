import os
import telebot
import sys
import json
import requests
from dotenv import load_dotenv

print(sys.prefix)

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

file_path = "heroStats.json" 

with open(file_path, "r") as file:
    data = json.load(file)

hero_dict = {hero["localized_name"]: hero["id"] for hero in data}

#print(hero_dict)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hey, nice to meet you, how may I assist you?")

# Message handler for hero stats
@bot.message_handler(commands=['hero-stats'])
def sign_handler(message):
    text = "What hero are you interested in?\nType its name like this: *Anti-Mage*, *Crystal Maiden*, etc."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_hero)

def fetch_hero(message):
    selected_hero = message.text
    #print("SELECTED HERO: " + selected_hero)

    headers = {"Content-Type": "application/json; charset=utf-8"}
    output = requests.get("https://api.opendota.com/api/heroStats",headers=headers, timeout=None)
    data = json.loads(output.content)

    for hero in data:
        print(hero)
        if hero["localized_name"] == selected_hero:
            hero_message = (
                f'*Hero:* {hero["localized_name"]}\n'
                f'*Primary attribute:* {hero["primary_attr"]}\n'
                f'*Attack type:* {hero["attack_type"]}\n'
                f'*Roles:* {hero["roles"]}\n'
                f'*Base health:* {hero["base_health"]}\n'
                f'*Base health regen:* {hero["base_health_regen"]}\n'
                f'*Base mana:* {hero["base_mana"]}\n'
                f'*Base mana regen:* {hero["base_mana_regen"]}\n'
                f'*Base armor:* {hero["base_armor"]}\n'
                f'*Base magic resistance (MR):* {hero["base_mr"]}%\n'
                f'*Base attack damage:* {hero["base_attack_min"]} - {hero["base_attack_max"]}\n'
                f'*Base strength:* {hero["base_str"]} (Gain: {hero["str_gain"]})\n'
                f'*Base agility:* {hero["base_agi"]} (Gain: {hero["agi_gain"]})\n'
                f'*Base intelligence:* {hero["base_int"]} (Gain: {hero["int_gain"]})\n'
                f'*Attack range:* {hero["attack_range"]}\n'
                f'*Projectile speed:* {hero["projectile_speed"]}\n'
                f'*Attack rate:* {hero["attack_rate"]}\n'
                f'*Base attack time:* {hero["base_attack_time"]}\n'
                f'*Attack point:* {hero["attack_point"]}\n'
                f'*Movement speed:* {hero["move_speed"]}\n'
                f'*Turn rate:* {hero["turn_rate"] if hero["turn_rate"] is not None else "N/A"}\n'
                f'*CM enabled:* {"Yes" if hero["cm_enabled"] else "No"}\n'
                f'*Number of legs:* {hero["legs"]}\n'
                f'*Day vision range:* {hero["day_vision"]}\n'
                f'*Night vision range:* {hero["night_vision"]}\n'
            )
            bot.send_message(message.chat.id, "Here are the requested stats!")
            bot.send_message(message.chat.id, hero_message, parse_mode="Markdown")

# Message handler for hero matchups
@bot.message_handler(commands=['hero-matchups'])
def sign_handler(message):
    text = "What hero are you interested in?\nType its name like this: *Anti-Mage*, *Crystal Maiden*, etc."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_hero_matchups)


def fetch_hero_matchups(message):
    selected_hero = message.text
    #print("SELECTED HERO: " + selected_hero)
    print(hero_dict[selected_hero])
    headers = {"Content-Type": "application/json; charset=utf-8"}
    output = requests.get(f"https://api.opendota.com/api/heroes/{hero_dict[selected_hero]}/matchups?",headers=headers, timeout=None)
    data = json.loads(output.content)
    top_10_data = data[:10]

    for item in top_10_data:
        hero_id = item["hero_id"]
        item["hero_name"] = next((name for name, id in hero_dict.items() if id == hero_id), None)
        del item["hero_id"]
    
    telegram_message = "\n\n".join(
        f"*Hero Name:* {item['hero_name']}\n"
        f"*Games Played:* {item['games_played']}\n"
        f"*Wins:* {item['wins']}"
        for item in top_10_data
    )
    bot.send_message(message.chat.id, "Here are the requested stats!")
    bot.send_message(message.chat.id, telegram_message, parse_mode="Markdown")

bot.infinity_polling()
