# RUNNER: Main runner
from loaddata import *
import json
import requests

def main():
    # DATA SOURCING:
    
    # IF TESTING:
    # loaddata()
    data = json.load(open('data/data.json'))
    
    # IF EXECUTION:
    # data = requests.get('https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=decimal&apiKey=2aa86d6b0c26a31df201c7909ed9253c')

    # CALCULATE SOME IDEAL BETS AND PRINT:
    for id in data:
        print(id['sport_key'])
        for bookmaker in id['bookmakers']:
            bookmaker_name = bookmaker['title']
            for market in bookmaker['markets']:
                if market['key'] == 'h2h':
                    print(bookmaker_name)
                    print(market['outcomes'])

if __name__ == "__main__":
    main()