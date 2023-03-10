def allMatches():
    jogos=[]
    clubes=(["FCP", "SCP", "SLB"])
    for i in range(len(clubes)):
        for j in range(len(clubes)):
            if i==j:
                continue
            jogos.append( (clubes[i], clubes[j]))
    return jogos
