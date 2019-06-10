url = requests.get("https://" + serverid + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + accountid + "?api_key=" + apikey)
matchhistory = url.json()

history = []
i = 0
#print(matchhistory)
#print("\n")

for match in matchhistory["matches"]:
    history.append(match["gameId"])
    i = i + 1
    if i == 19:
        break

i = 0
partida = 1
while(int(partida)>0 and int(partida)<20):
    for match in matchhistory["matches"]:    
        for x,y in dictchampid.items():
            if int(match["champion"]) == int(y):
                if str(match["role"]) == "NONE":
                    role = ""
                elif str(match["role"]) == "DUO":
                    role = ", Duo"
                else:
                    role = ", Solo"
                print("{}- Jogado como {} na lane {}{}\n" .format(i, x, match["lane"], role))
        if i == 19:
            break
        i = i + 1
    partida = input("Ver detalhes de qual partida? ")
    print("\n\n")
    game = history[int(partida)]
    url = requests.get("https://" + serverid + ".api.riotgames.com//lol/match/v4/matches/"+ str(game) + "?api_key=" + apikey)
    match = url.json()
    
    print(match)
    i = 0
    
################################### Fazer um tratamento do output da descrição da partida, é basicamente um print bem estruturado
################################### Talvez incrementar o histórico para mostrar Summoner spells, runas e etc