import json
import requests

url = requests.get("https://ddragon.leagueoflegends.com/cdn/8.19.1/data/en_US/champion.json")
champsid = url.json()

dictchampid = {}

for champ in champsid['data']:
    dictchampid[champ] = champsid['data'][champ]['key']
    
#print(dictchampid)
for x, y in dictchampid.items():
    print("{}: {} ".format(x, y))
#print(champsid['data']['Renekton'])