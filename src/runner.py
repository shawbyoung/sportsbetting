# runner: main runner
from loaddata import *
from Bet import *

import json
import requests

def main():
    # DATA SOURCING:
    
    # If TESTING:
    # loaddata()
    data = json.load(open('data/data.json'))
    
    # IF EXECUTION:
    # data = requests.get('https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=american&apiKey=2aa86d6b0c26a31df201c7909ed9253c')

    # CALCULATE SOME IDEAL BETS AND PRINT:
    for id in data:
        for broker in id["bookmakers"]:
            markets = broker["markets"]
            # print(markets)

if __name__ == "__main__":
    main()
