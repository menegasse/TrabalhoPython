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

# Variáveis necessárias
i = 0
p = 0
ban = 0
j = 0

placar1 = "Jorge"
placar2 = "bla"

banstime1 = []
banstime2 = []

jogador = []
spells = []
jogadorKDA = []
KDA = ""

torrestime1 = 0
torrestime2 = 0

inibidorestime1 = 0
inibidorestime2 = 0

dragtime1 = 0
dragtime2 = 0

barontime1 = 0
barontime2 = 0

arautotime1 = 0
arautotime2 = 0

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
    
    placar1 = str(match["teams"][0]["win"])
    
    # Principais objetivos do time 1:
    dragtime1 = match["teams"][0]["dragonKills"]
    barontime1 = match["teams"][0]["baronKills"]
    torrestime1 = match["teams"][0]["towerKills"]
    inibidorestime1 = match["teams"][0]["inhibitorKills"]
    arautotime1 = match["teams"][0]["riftHeraldKills"]
    
    # Principais objetivos do time 2:
    dragtime2 = match["teams"][1]["dragonKills"]
    barontime2 = match["teams"][1]["baronKills"]
    torrestime2 = match["teams"][1]["towerKills"]
    inibidorestime2 = match["teams"][1]["inhibitorKills"]
    arautotime2 = match["teams"][1]["riftHeraldKills"]
    
    # Bans:
    for b in range(5):
        banstime1.append(int(match["teams"][0]["bans"][ban]["championId"]))
        banstime2.append(int(match["teams"][1]["bans"][ban]["championId"]))
        ban = ban  + 1
    
    ban = 0
    for item in banstime1:
        for x,y in dictchampid.items():
            if int(item) == int(y):
                banstime1[ban] = x
                ban = ban + 1
    
    ban = 0
    for item in banstime2:
        for x,y in dictchampid.items():
            if int(item) == int(y):
                banstime2[ban] = x
                ban = ban + 1
    
    if placar1 == "Fail":
        placar1 = "Derrota"
        placar2 = "Vitória"
    else:
        placar1 = "Vitória"
        placar2 = "Derrota"
        
    #spells.append(match["participants"][int(j)]["spell1Id"])
    #spells.append(match["participants"][int(j)]["spell2Id"])
        
    # Puxa KDA
    for j in range(10):
        KDA = ""
        KDA = str(match["participants"][int(j)]["stats"]["kills"])
        KDA = KDA + "/" + str(match["participants"][int(j)]["stats"]["deaths"])
        KDA = KDA + "/" + str(match["participants"][int(j)]["stats"]["assists"])
        jogadorKDA.append(KDA)
        
    for j in range(10):
        for x,y in dictchampid.items():
            if int(match["participants"][int(j)]["championId"]) == int(y):
                jogador.append(x)
            
        
    print("\n\n\n\n\n\n\n\tTime aliado: ({})\n" .format(placar1))
    for p in range(10):
        print("Campeão: {}. KDA: {}. Jogador: {}" .format(jogador[p], jogadorKDA[p], match["participantIdentities"][p]["player"]["summonerName"]))
        
        if p == 4:
            print("\nTorres destruídas: {}, Inibidores destruídos: {}, Dragões feitos: {}, Arautos feitos: {} Barões feitos: {}" .format(torrestime1, inibidorestime1, dragtime1, arautotime1, barontime1))
            print("Bans: {}, {}, {}, {}, {}" .format(banstime1[0], banstime1[1], banstime1[2], banstime1[3], banstime1[4]))
            print("\n\n\tTime adversário: ({})\n" .format(placar2))
    #print("\nBans: {}, {}, {}" .format(banstime2[0], banstime2[1], banstime2[2]))
    print("\nTorres destruídas: {}, Inibidores destruídos: {}, Dragões feitos: {}, Arautos feitos: {} Barões feitos: {}" .format(torrestime2, inibidorestime2, dragtime2, arautotime2, barontime2))
    print("Bans: {}, {}, {}, {}, {}" .format(banstime2[0], banstime2[1], banstime2[2], banstime2[3], banstime2[4]))
    i = 0
    print("\n\n")
    break
    
################################### Talvez incrementar o histórico para mostrar Summoner spells, runas e etc
