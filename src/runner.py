# RUNNER: Main runner
import json

from loaddata import *
from findbestodds import *

def main():
    # GETS DATA FROM API 
    # fname  = load_and_save()
    fname = 'data0'
    data = json.load(open('data/' + fname + '.json'))
    
    # CALCULATE SOME IDEAL BETS AND PRINTS
    findbestodds(data)

if __name__ == "__main__":
    main()