# LOADDATA: Loads API data into a JSON for testing
import requests
import json

def load_data_for_testing(): 
    # CALLS THE API 
    apiKey = ""
    with open('src/api_key.txt') as f:
        apiKey = f.readlines()
    req = requests.get('https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=decimal&apiKey=' + apiKey[0])

    # LOADS IT INTO A FILE IN DATA DIRECTORY 
    with open('data/data.json', 'w') as f:
        json.dump(req.json(), f)

def load_data_execute():
    # CALLS THE API 
    apiKey = ""
    with open('src/api_key.txt') as f:
        apiKey = f.readlines()
    return requests.get('https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=decimal&apiKey=' + apiKey[0])