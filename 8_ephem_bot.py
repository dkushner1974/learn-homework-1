"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem, datetime


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet(update, context):
    date = datetime.datetime.now()
    planet_dict = [name for _0, _1, name in ephem._libastro.builtin_planets()]
    text = update.message.text
    print('Вызов /planet')
    if len(text.split()) == 2:
        user_planet = text.split()[-1].capitalize()
        if user_planet in planet_dict:
            cons = getattr(ephem, user_planet)(date)
            planet = (('Планета {} сейчас в созвездии '.format(user_planet)) + str(ephem.constellation(cons)))  
        else:
            planet = 'Нет такой планеты в словаре'      
    else:
        planet = 'Это точно не планета'
    update.message.reply_text(planet)

def main():
    mybot = Updater("5714257774:AAGnJCYRUhEev7HrMBp208wjHWw-cOhymH0", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
