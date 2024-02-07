import requests
from flask import Flask

app = Flask(__name__)

def vær(sted):
    url =f"https://www.wttr.in/{sted}?format=j1"
    respons = requests.get(url)
    data = respons.json()

    data["current_condition"][0]["FeelsLikeC"]#føles som
    værtype = data["current_condition"][0]["weatherDesc"][0]["value"]#værtypen
    tempratur = data["current_condition"][0]["temp_C"]#antall grader
    return værtype, tempratur

@app.get("/")
def hjem():
    return "Hei på deg!"

@app.get("/<string:sted>")
def rute_sted(sted: str):
    værtype, tempratur = vær(sted)
    return f"I {sted} er det {værtype} og {tempratur} grader"


app.run(debug=True)