# LOADDATA: Loads API data into a JSON for testing
import requests
import json

def loaddata(): 
    # CALLS THE API 
    req = requests.get('https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=decimal&apiKey=2aa86d6b0c26a31df201c7909ed9253c')

    # LOADS IT INTO A FILE IN DATA DIRECTORY 
    with open('data/data.json', 'w') as f:
        json.dump(req.json(), f)