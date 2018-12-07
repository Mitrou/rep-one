import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Попетросяним, блеать!")


@bot.message_handler(commands=["stop"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Попетросянили, блеать...")


@bot.message_handler(content_types=["text"])
def trista(message):
    print(message.text)
    try:
        if '300' == message.text or '300' in message.text  or 'триста' in str(message.text).lower():
            bot.send_message(message.chat.id, "Отсоси у тракториста!")
    except:
        bot.send_message(message.chat.id, "Боту плохо, бот всё.")


if __name__ == '__main__':
    bot.polling(none_stop=True)
