from typing import Tuple


def calculateReturn(best_odds_home, best_odds_away ):
    f = 0
    u = 0
    
    if best_odds_home > best_odds_away:
        f = best_odds_away
        u = best_odds_home
    else:
        f = best_odds_home
        u = best_odds_away

    return (f - (f/u) - 1) / (1 + (f/u))

def calculateBetAmts(betAmt, best_odds_home, best_odds_away) -> Tuple:
    f = 0
    u = 0
    
    if best_odds_home > best_odds_away:
        f = best_odds_away
        u = best_odds_home
    else:
        f = best_odds_home
        u = best_odds_away
    
    favoriteAndUnderdog = tuple()
    favoriteAndUnderdog[0] = betAmt / ((f/u) + 1 )
    favoriteAndUnderdog[1] = (betAmt*f) / (f + u)

    return favoriteAndUnderdog

    