import json
import requests

url = requests.get("https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId + "?api_key=" + apikey)
masteries = url.json()

i = 0
bau = "Sim"

print("\t10 Melhores campeões: \n")
for champ in masteries:
    for x,y in dictchampid.items():
        if int(champ["championId"]) == int(y):
            if champ["chestGranted"] == False:
                bau = "Sim"
            else:
                bau == "Não"
            print("Campeão: {} \nNível de Maestria: {} \nPontos de Maestria: {} \nGanhou baú: {}\n\n" .format(x, champ["championLevel"], champ["championPoints"], champ["chestGranted"]))
    i = i +1
    if i>10:
        break


######### Preciso fazer a comparação Booleana pra traduzir a resposta de ganhou baú ou não