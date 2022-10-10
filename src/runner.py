# RUNNER: Main runner
from prettytable import PrettyTable
import json

from loaddata import *
from findbestodds import *

def main():
    
    # GETS DATA FROM API 
    fname  = 'ZaKyWiPaPc'
    data = json.load(open('data/' + fname + '.json'))
    
    # CALCULATE SOME IDEAL BETS AND PRINTS
    findbestodds(data)

    
        
if __name__ == "__main__":
    main()