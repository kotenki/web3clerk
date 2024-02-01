import logging
import json
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

data = cg.get_coins_list()
count = 0
#data = json.loads(json_data)

for i in data:
    count = count + 1
    #print("\"" + i["id"].upper() + "\" : \"" + i["symbol"].upper() + "\"")
    #rank = cg.get_coin_by_id(data[1]["id"])["market_cap_rank"]
    #if (rank) < 200: 
    print("\"" + i["id"].upper() + "\": \"" + i["symbol"].upper() + "\",")
    #print(str(count) + "...")

print("Total tokens processed: " + str(count))
