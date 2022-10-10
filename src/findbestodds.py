from print_outcomes import *

def findbestodds(data):
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
        
        outcomes = {}

        # For each bookmaker offering bets
        for bookmaker in id['bookmakers']:
            bookmaker_name = bookmaker['title']

            # For each kind of bet, find max bet odd (most buying power) for head to head bets
            
            for market in bookmaker['markets']:
                if market['key'] == 'h2h':
                    outcomes = market['outcomes']

            if not outcomes:
                continue

            for bet in outcomes:
                price = abs(bet['price'])
                
                if bet['name'] == home_team:    
                    if price >= best_odd_home:
                        broker_home = bookmaker_name
                        best_odd_home = price

                elif bet['name'] == away_team:    
                    if price >= best_odd_away:
                        broker_away = bookmaker_name
                        best_odd_away = price
                
                elif bet['name'] == 'Draw':
                    if price >= best_odd_draw:
                        broker_draw = bookmaker_name
                        best_odd_draw = price            
        
        # Calculates indicator 
        prob = 0
        if ( best_odd_draw > 1 ):
            prob += (1/best_odd_draw) 
        prob += (1/best_odd_home) + (1/best_odd_away)  

        # If prob < 1, there is arbitrage 
        if( prob < 1 ): 
            if( broker_draw == ''):
                print_outcomes(home_team, broker_home, best_odd_home, away_team, broker_away, best_odd_away, 100) 
            else:
                print()
            print() 

