# RUNNER: Main runner
from prettytable import PrettyTable
from loaddata import *
from print_outcomes import *
import json

def main():
    # DATA SOURCING:
    
    # IF TESTING:
    load_data_for_testing()
    # 
    data = json.load(open('data/data.json'))
    
    # IF EXECUTION:
    # data = load_data_execute()

    # CALCULATE SOME IDEAL BETS AND PRINT:
    # For each game
    for id in data:
        # Instantiate variables that'll represent strongest betting odds
        best_odd_home = 1
        best_odd_away = 1
        best_odd_draw = 1
        
        broker_home = ""
        broker_away = ""
        broker_draw = ""

        home_team = id['home_team']
        away_team = id['away_team']
        
        # For each bookmaker offering bets
        for bookmaker in id['bookmakers']:
            bookmaker_name = bookmaker['title']

            # For each kind of bet, find max bet odd (most buying power) 
            for market in bookmaker['markets']:
                
                # If head to head,
                if market['key'] == 'h2h':
                    outcomes = market['outcomes']

                    for bet in outcomes:
                        if bet['name'] == home_team:    
                            if bet['price'] >= best_odd_home:
                                broker_home = bookmaker_name
                                best_odd_home = bet['price']

                        if bet['name'] == away_team:    
                            if bet['price'] >= best_odd_away:
                                broker_away = bookmaker_name
                                best_odd_home = bet['price']
                        
                        if bet['name'] == 'Draw':
                            if bet['price'] >= best_odd_draw:
                                broker_draw = bookmaker_name
                                best_odd_home = bet['price']
        
        # Calculates indicator 
        prob = 0
        if ( best_odd_draw > 1 ):
            prob += (1/best_odd_draw) 
        prob += (1/best_odd_home) + (1/best_odd_away)  

        # If prob < 1, there is arbitrage 
        # if( prob < 1 ): 

        if( broker_draw == ''):
            print_outcomes(home_team, broker_home, best_odd_home, away_team, broker_away, best_odd_away, 100) 
        
        print('_' * 10) 



        
if __name__ == "__main__":
    main()