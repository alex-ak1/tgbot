import telebot
import json

settings = json.load(open("settings.json"))
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

