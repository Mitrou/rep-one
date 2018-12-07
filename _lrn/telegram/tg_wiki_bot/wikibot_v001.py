import telebot
import config
from backendv001 import WikiAPI

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id, "Привет, я плохо, но умею лазить в англоязычную википедию и искать чо. Команды "
                                      "пока /start (Ваш КО) и /reset (обе просто для лулзов). Предлагаю искать чо.")


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "Ну и хрен с тобой.")


@bot.message_handler(content_types=["text"])
def get_wiki_item(message):
    try:
        bot.send_message(message.chat.id, WikiAPI.wiki_summary_by_name(message.text))
    except:
        bot.send_message(message.chat.id, "Инглиш мадафака, дю ю спик ит? (Ну или нет такой статьи)")
    print(message.text)



if __name__ == '__main__':
    bot.polling(none_stop=True)
