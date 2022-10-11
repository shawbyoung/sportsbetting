from faulthandler import cancel_dump_traceback_later
from prettytable import PrettyTable
from odds_functions import *

def print_outcomes(home_team, broker_home, best_odd_home, away_team, broker_away, best_odd_away, bet_amt):

    
    odds_and_brokers = PrettyTable()
    outcomes = PrettyTable()
    
    fav_odd = -1
    und_odd = -1
    fav_t = ''
    und_t = ''
    
    if best_odd_home > best_odd_away:
        und_odd = best_odd_home
        fav_odd = best_odd_away
        
        und_t = home_team
        fav_t = away_team

        und_bk = broker_home
        fav_bk = broker_away

    else: 
        fav_odd = best_odd_home
        und_odd = best_odd_away

        fav_t = home_team
        und_t = away_team

        fav_bk = broker_home
        und_bk = broker_away
        
    
    odds_and_brokers.field_names = ["Bet Amt",  und_t + " odds", fav_t + " odds", ""]
    odds_and_brokers.add_row([bet_amt, str(und_odd) + ": " + und_bk, str(fav_odd) + ": " + fav_bk,""])
    
    outcomes.field_names = ['Outcome','Profit of bet on ' + und_t, 'Profit of bet on' + fav_t, 'Net']

    bet_amts = calculateBetAmts(bet_amt,fav_odd,und_odd) 
    bet_f,bet_u = bet_amts
    


    u_row = [und_t]
    u_row.append( str(bet_u) + '*' + str(und_odd) + str(' - ') + str(bet_u) + str(' = ') + str( bet_u*und_odd - bet_u) )
    u_row.append( str(-1*bet_f) )
    u_row.append( str(bet_u) + '*' + str(und_odd) + str(' - ') + str(bet_u) + '-' + str(bet_f) + ' = ' + str(bet_u*und_odd - bet_u - bet_f))
    outcomes.add_row(u_row)

    f_row = [fav_t]
    f_row.append( str(-1*bet_u) )
    f_row.append( str(bet_f) + '*' + str(fav_odd) + ' - ' + str(bet_f) + '=' + str(bet_f*fav_odd - bet_f))
    f_row.append( str(bet_f) + '*' + str(fav_odd) + ' - ' + str(bet_f) + ' - ' + str(bet_u) + '=' + str(bet_f*fav_odd - bet_f - bet_u))
    outcomes.add_row(f_row)

    ret = calculateReturn(fav_odd,und_odd)
    print(f"{ret:.0%}")
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