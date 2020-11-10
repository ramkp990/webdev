import json
stocks = []

with open('3.txt', 'r') as data:
    for line in data:
        line = line.strip()
        ldata = line.split(',')
        temp_stock = {
            'name':ldata[0],
            'link':ldata[1],
        }
        stocks.append(temp_stock)
with open('3.json', 'w') as fp:
    json.dump(stocks, fp, indent=4)
from pprint import pprint
pprint(stocks)
