from typing import Tuple

def calculateReturn(f, u ):
    return (f - (f/u) - 1) / (1 + (f/u))

def calculateBetAmts(bet_amt, f, u) -> Tuple:
    favoriteAndUnderdog = []
    favoriteAndUnderdog.append(bet_amt / ((f/u) + 1 ))
    favoriteAndUnderdog.append((bet_amt*f) / (f + u))

    return favoriteAndUnderdog

    