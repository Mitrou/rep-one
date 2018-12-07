import telebot
import config
from backendv002 import WikiAPI

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
    print(message.text)  # kind of log in console
    syngle_article = WikiAPI.wiki_summary_by_name(message.text)
    list_refer = WikiAPI.wiki_refer_to(message.text)
    try:
        if 'may refer to' not in syngle_article:
            bot.send_message(message.chat.id, syngle_article)
        elif 'may refer to' in syngle_article:
                bot.send_message(message.chat.id, "Значений много, выбирай!")
                bot.send_message(message.chat.id, list_refer)
        else:
                bot.send_message(message.chat.id, "Unexpected error!")
    except:
        bot.send_message(message.chat.id, "Инглиш мадафака, дю ю спик ит? (Ну или нет такой статьи)")


if __name__ == '__main__':
    bot.polling(none_stop=True)
