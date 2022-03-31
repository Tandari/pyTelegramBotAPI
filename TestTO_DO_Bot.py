import telebot
import random

token = "5139808996:AAFNa5lH8oWHxtzGoTVvJ7uUDay-bNd3R18"

bot = telebot.TeleBot(token)

HELP = """
/help - список команд.
/add - добавить задачу в список (название задачи запраашиваем у пользователя).
/show - напечатать все добавленные задачи.
/random - добавлять случайную задачу на дату Сегодня."""

random_tasks = ["Лечть спать.", "Покормить кошку", "Умыться", "Почистить зубы"]

tasks={}

def add_todo(date, task):
  if date in tasks:
      tasks[date].append(task)
  else:
      tasks[date] = []
      tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "Сегодня"
    task = random.choice(random_tasks)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    text = ""
    if date in tasks:
      text.upper() + "\n"
      for task in tasks[date]:
          text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет."
    bot.send_messange(message.chat.id, text)



bot.polling(none_stop=True)
