from prettytable import PrettyTable

def print_outcomes(home_team, broker_home, best_odd_home, away_team, broker_away, best_odd_away, betAmt):

    odds_and_brokers = PrettyTable()

    odds_and_brokers.field_names = ["Bet Amt",  home_team + " odds: " + broker_home, away_team + " odds: " + broker_away]
    odds_and_brokers.add_row([betAmt, str(best_odd_home) + ": " + broker_home, str(best_odd_away) + ": " + broker_away])

    outcomes = PrettyTable()
    outcomes.field_names = ['Outcome','Profit of bet on ' + home_team, 'Profit of bet on' + away_team, 'Net']
    
    betOnHome = (betAmt*best_odd_home)-betAmt
    betOnAway = -1.0*betAmt
    net = betOnHome + betOnAway
    outcomes.add_row([home_team + 'wins', betOnHome, betOnAway, net])

    betOnHome = -1.0*betAmt
    betOnAway = (betAmt*best_odd_away)-betAmt
    net = betOnHome + betOnAway
    outcomes.add_row([away_team + 'wins', betOnHome, betOnAway, net])

    print(odds_and_brokers)
    print(outcomes)
    
# def print_outcomes(home_team, broker_home, best_odd_home, away_team, broker_away, best_odd_away, best_odd_draw, broker_draw, betAmt):

#     odds_and_brokers = PrettyTable()

#     odds_and_brokers.field_names = ["Bet Amt",  home_team + " odds: " + broker_home, away_team + " odds: " + broker_away, "Draw odds: " + broker_draw]
#     odds_and_brokers.add_row([betAmt, str(best_odd_home) + ": " + broker_home, str(best_odd_away) + ": " + broker_away, str(best_odd_draw) + ": " + broker_draw])

#     outcomes = PrettyTable()
#     outcomes.field_names = ['Outcome','Profit of bet on ' + home_team, 'Profit of bet on' + away_team, 'Net']
    
#     betOnHome = (betAmt*best_odd_home)-betAmt
#     betOnAway = -1.0*betAmt
#     betOnDraw = -1.0*betAmt
#     net = betOnHome + betOnAway
#     outcomes.add_row([home_team + 'wins', betOnHome, betOnAway, betOnDraw])
       
#     outcomes.add_row([away_team + 'wins',])
#     outcomes.add_row(['Draw',])