Sports Betting Bot

Get your own API from https://the-odds-api.com/ and put in a file called api_key.txt in your src directory. 

1.  HEDGING APPROACH 
    1.  Parse data from API.
    2.  Find optimal hedges... it's disgustingly simple.
        Take all available decimal odds, invert, sum, anything below 100%/1.0 
        is gold. Establish threshold of 'worthwhile' bets.
    3.  Once arbitrage is found, decide between no loss and max profit or guaranteed profit.  

2.  "ONE-CLICK" TRADING AUTOMATION 
    1.  Automate trading with selenium
        1.  Primary concern - hardcoding for different websites