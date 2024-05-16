import json 

with open ("transaksjoner.json", encoding="utf-8") as fil: 
    transaksjoner = json.load(fil)

antall_transaksjoner = {}
for transaksjon in transaksjoner: 
    for sted in transaksjon['beskrivelse']: 
        if sted in antall_transaksjoner:
            antall_transaksjoner[sted] += 1 
        else:
            antall_transaksjoner[sted] = 1 

sortert = sorted(antall_transaksjoner.items(), key=lambda sted: sted[1], reverse= True)
print(sortert)
for i in range(3): 
    print(f"{i + 1}: {sortert[i][0]} - {sortert[i][1]} transaksjoner") 
        

