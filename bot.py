import telebot
import json
import sys
from pathlib import Path

settings = json.load(open( str(Path(__file__).parent) + "/settings.json"))
if (settings.get('tgtoken', '') == ''):
    print( "No bot token specified" )
    exit(1)

bot = telebot.TeleBot(settings['tgtoken'])

def saveSettings():
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=2)

@bot.message_handler(commands=['start'])
def waitUser(msg):
    print( msg )

    settings['tguser'] = msg.from_user.id
    saveSettings()

    bot.send_message(msg.from_user.id, 'hello')
    bot.stop_bot()

    print( f"User {msg.from_user.id} registered" )

    exit(1)

def register():
    print( f"Say /start to bot https://t.me/{bot.user.username}?start=start" )
    bot.polling(none_stop=True, interval=0)

def sendMsg(msg):
    if (settings.get("tguser", "") == ""):
        print( "Register tg bot first" )
        exit(1)

    bot.send_message(settings['tguser'], msg)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print( "usage: python3 bot.py \"some message to user\"" )
        exit(1)

    msg = sys.argv[1]

    print( f" Send {msg}" )
    sendMsg(msg)