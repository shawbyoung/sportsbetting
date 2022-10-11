# LOADDATA: Loads API data into a JSON for testing
import requests
import json
import random
import datetime

def load_and_save(): 
    # CALLS THE API 
    apiKey = ""
    with open('src/api_key.txt') as f:
        apiKey = f.readlines()
    req = requests.get('https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=decimal&apiKey=' + apiKey[0])

    fname = str(datetime.datetime.now())
    fname = fname.replace("\\s+", "")
    fname = fname.replace(":", "-")
    fname = fname.replace(".", "-")
    # ct stores current time
    
    # LOADS IT INTO A FILE IN DATA DIRECTORY 
    with open('data/'+ fname + '.json', 'w') as f:
        json.dump(req.json(), f)
    
    return fname
    
def load_data_execute():
    # CALLS THE API 
    apiKey = ""
    with open('src/api_key.txt') as f:
        apiKey = f.readlines()
    return requests.get('https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=decimal&apiKey=' + apiKey[0])