import json
import requests

url = requests.get("https://br1.api.riotgames.com/lol/platform/v3/champion-rotations/?api_key=" + apikey)
champsrotation = url.json()

#print(champsrotation)

print("\nListagem de campeões grátis da semana:")
for champ in champsrotation['freeChampionIds']:
    for x,y in dictchampid.items():
        if int(champ) == int(y):
            print(x)
            
print("\nGrátis apenas para novos jogadores: ")
for champ in champsrotation['freeChampionIdsForNewPlayers']:
    for x,y in dictchampid.items():
        if int(champ) == int(y):
            print(x)
            