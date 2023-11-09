from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog, leaguedashptteamdefend, boxscoredefensive, leaguegamefinder, boxscorematchups
from nba_api.stats.endpoints import defensehub, draftboard, drafthistory, playerawards, playercareerstats, gamerotation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

"""
This is where the features will be created and saved.
The overall Structure of the data should be:
    - each row represents a player's and team's stats going into a game. 
"""

# This method gets average player stats of categories passed in, if exists.

def getAveragePlayerStats(data, categories):
    clean_categories_filter = filter(lambda col : col in data.columns, categories)
    clean_categories = list(clean_categories_filter)
    all_players = []
    for player_id in data["Player_ID"].unique():
        player_stats = data.loc[data['Player_ID'] == player_id]
        for category in clean_categories:
            avg_col_name = f'AVG_{category}'
            player_stats[avg_col_name] = player_stats.groupby('SEASON_ID')[category].expanding().mean().shift(1).reset_index(0,drop=True)
            player_stats[avg_col_name] = player_stats[avg_col_name].fillna(player_stats[category])
        all_players.append(player_stats)

    full_player_stats = pd.concat(all_players, ignore_index=True)
    return full_player_stats

def collectPlayerFeatures(data, categories, model_name):
    currPath = os.path.dirname(__file__)
    fullDataPath = os.path.join(currPath, '../../datasets/raw_data.csv')
    full_data = pd.read_csv(os.path.normpath(fullDataPath))


if __name__ == "__main__":
    pd.options.mode.chained_assignment = None
    categories = ['PTS', 'REB', 'AST', 'MIN']
    raw_data = pd.read_csv('../../datasets/raw_data.csv')
    stats_df = getAveragePlayerStats(raw_data, categories)
    stats_df.to_csv('../../datasets/raw_data.csv', index=False)