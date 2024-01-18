fil = open("tullefil.txt", encoding="utf8")
data = fil.read()
fil.close()

linjer = data.split("\n")

print(data)

#lese json filer 
import json 

fil = open("sanger.json", encoding="utf-8")
sanger = json.load(fil)
fil.close 


with open("sanger.json", encoding="utf-8") as fil:
    sanger = json.load(fil)

print(sanger[0])
