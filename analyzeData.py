import pandas as pd 
import numpy as np 


nbaStandings = pd.read_csv('NbaStandings2019Dataset.csv')
nbaPlayers = pd.read_csv('NBA_Players.csv')
#print(nbaStandings)

# Removes leading spaces from column names
nbaPlayers.columns = [col.strip() for col in nbaPlayers.columns]
nbaPlayers = nbaPlayers[['TEAM', 'NAME', 'AGE', 'EXPERIENCE', 'HT']]
nbaPlayers.columns = ['TEAM', 'NAME', 'AGE', 'EXPERIENCE', 'HEIGHT']
print(nbaPlayers)

