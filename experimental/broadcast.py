from keys import TG_API_KEY
import telebot
import logging
import database


logging.basicConfig(filename="bot.log", level=logging.DEBUG, format="%(asctime)s %(message)s", filemode="w")

bot = telebot.TeleBot(TG_API_KEY)

connection = database.connect()

# add function get_all_chats to database lib
chats = database.get_all_chats(connection)

for c in chats: 
    #msg = "Hi there! I got an update!\nMy commands have changed to: \n\n" + "/add - to add a new alert\n" + "/myalerts - to get the list of all alerts\n\n" + "You can also access a quick menu in the chat instead of typing them. \nTry it out!"
    msg = "Привет, хозяин! Я снова в строю!"
    bot.send_message(c[0], msg)
    #print("=====")
    #print(c[0])
    #print(c[1])
    #print(msg)
