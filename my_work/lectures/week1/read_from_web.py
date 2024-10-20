# program to read from the web
# author: Atacan Buyuktalas

import requests 

url ="https://api.coindesk.com/v1/bpi/currentprice.json" # this is the url of the api
response = requests.get(url) # get the response from the url    
data = response.json()  # get the json data from the response
print (data['bpi']['EUR']['rate_float'])  # print the value of the bitcoin in euros