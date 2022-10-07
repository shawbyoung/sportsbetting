import xgboost
import numpy as np
import pandas as pd
import requests

req = requests.get('https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&oddsFormat=american&apiKey=2aa86d6b0c26a31df201c7909ed9253c')

print(req.json()) 