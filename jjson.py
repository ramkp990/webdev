import json
stocks = []

with open('videolink', 'r') as data:
    for line in data:
        line = line.strip()
        ldata = line.split(',')
        temp_stock = {
            'name':ldata[0],
            'link':ldata[1],
        }
        stocks.append(temp_stock)
with open('video.json', 'w') as fp:
    json.dump(stocks, fp, indent=4)
from pprint import pprint
pprint(stocks)
