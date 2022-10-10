Sports Betting Bot

Get your own API from https://the-odds-api.com/ and put in a file called api_key.txt in your src directory. 

1.  HEDGING APPROACH 
    a.  Parse data
    b.  Find optimal hedges... it's disgustingly simple.
        Take all available decimal odds, invert, sum, anything below 100%/1.0 
        is gold. Establish threshold of 'worthwhile' bets. 

2.  "ONE-CLICK" TRADING AUTOMATION 
    a.  Automate trading with selenium
        x.  Primary concern - hardcoding for different websites