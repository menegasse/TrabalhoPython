import json
import requests
from os import system

servers = {"BR": "br1",
           "EUNE": "eun1",
           "EUW": "euw1",
           "JP": "jp1",
           "KR": "kr",
           "LAN": "la1",
           "LAS": "la2",
           "NA": "na1",
           "OCE": "oc1",
           "TR": "tr1",
           "RU": "ru",
           "PBE": "pbe1"}

apikey = "RGAPI-777a179e-6c24-4218-804a-74f2190a9f94"

escolheserver = 0

while(escolheserver == 0):
    print("\n\n\nServidores disponíveis: \n")
    for i in servers:
        print(i)
    server = input("\nQual o servidor? \n")
    
    for x, y in servers.items():
        if server == x:
            serverid = y
            escolheserver = 1
            break
    
print("\n")
nick = input("Digite o nome a ser pequisado: \n")

url = requests.get("https://" + serverid + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + nick +"?api_key=" + apikey)
player = url.json()

#print("\n")
#print(player)

summonerId = player["id"]

print("\n")

for att, valor in player.items():
    if att=="name":
        print("Nome: %s" %(valor))
    if att=="summonerLevel":
        print("Nível: %s" %(valor))
        
#print("\n")

#for x, y in player.items():
    #print("{}: {} ".format(x, y))
    

###########    Colocar tratamento de maiusculo no nome do servidor
###########    Colocar tratamento de espaços no nome do jogador