import time
import logging
logging.basicConfig(filename="walletscan.log", level=logging.DEBUG, format="%(asctime)s %(message)s", filemode="w")
import telebot
from keys import TG_API_KEY, ETHERSCAN_API_KEY
from etherscan import Etherscan # https://github.com/pcko1/etherscan-python

# Goerli: 
eth = Etherscan(ETHERSCAN_API_KEY, net="goerli")
# Mainnet:
eth = Etherscan(ETHERSCAN_API_KEY)

from help import *
from constants import *
import database as db
from datetime import datetime

bot = telebot.TeleBot(TG_API_KEY)

conn = db.connect()


def getAcctTransactions(account, start):
    
    alerts = {}

    try:
        transactions = eth.get_erc20_token_transfer_events_by_address(address=account, startblock=start, endblock="", sort="asc")
        
        for tx in transactions: 
            token = tx["tokenSymbol"]
            amount = str(round(int(tx["value"])/pow(10, int(tx["tokenDecimal"])), 2))

            if account.casefold() == tx["from"].casefold():
                direction = " sent to "
                account_deal = tx["to"]      
            elif account.casefold() == tx["to"].casefold():
                direction = " received from "
                account_deal = tx["from"]

            alertText = amount + " " + token + direction + account_deal

            alerts[tx["blockNumber"]] = alertText
    except:
        logging.warning("No transactions found for account " + account + " from block " + str(start) )

    return alerts

def getAccounts():
    return db.get_accounts(conn)

while True: 

    for record in getAccounts(): 

        chat_id = record[0]
        account = record[1]
        startblock = record[2]
        alerts = getAcctTransactions(account, startblock + 1)

        for block in alerts: 
            bot.send_message(chat_id, alerts[block])
            db.set_block_number(conn, account, block)
    
    time.sleep(10)


 



