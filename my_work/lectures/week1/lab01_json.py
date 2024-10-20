# lab01 - JSON file reading from web
# author: Atacan Buyuktalas

import requests

url ="https://api.coindesk.com/v1/bpi/currentprice.json" 
response = requests.get(url) 
data = response.json()  
# print (type(data)) 
print(data['bpi']['EUR']['rate'])