from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog, leaguedashptteamdefend, boxscoredefensive, leaguegamefinder, boxscorematchups
from nba_api.stats.endpoints import defensehub, draftboard, drafthistory, playerawards, playercareerstats, gamerotation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Collect raw data from the API.

"""
def getSinglePlayerData(player_id):
    player_log = playergamelog.PlayerGameLog(player_id=player_id, season=SeasonAll.all, season_type_all_star='Regular Season')
    player_df = player_log.get_data_frames()[0]
    
    if player_df.empty: # Check if dataframe is empty
        return None
    
    player_flipped = player_df.iloc[::-1].reset_index(drop=True)
    
    return player_flipped

def collectAllPlayerData(num_players):
    all_players = players.get_players()
    all_players_df = pd.DataFrame(all_players)

    active_players_df = all_players_df[all_players_df['is_active'] == True]

    players_to_use = active_players_df.sample(n=num_players)

    all_player_data = []

    # Loop over players
    for _, player in players_to_use.iterrows():
        player_data = getSinglePlayerData(player['id'])
        if player_data is not None: # Check if player_data is not None
            all_player_data.append(player_data)
    all_data_df = pd.concat(all_player_data, ignore_index=True)
    all_data_df.to_csv('../../datasets/raw_data.csv', index=False)

if __name__ == "__main__":
    print("Compiling all player data into raw player data.")
    collectAllPlayerData(300)






# Prepare the features and labels

# MOST ADVANCED STATS API ENDPOINTS ARE NOT FUNCTIONAL ATM.

# Get game-by-game stats for every single player. 



# Select a subset of players for testing. You can modify this.

# Combine all dataframes


# Fetch team defensive stats for a season

#team_defense = leaguedashptteamdefend.LeagueDashPtTeamDefend(season='2022-23')
#team_defense_df = team_defense.get_data_frames()[0]
#print(team_defense_df)

# BOX SCORE DEFENSE NOT WORKING FOR NOW.
# box_defense = boxscoredefensive.BoxScoreDefensive(game_id = '0022201228')
# box_defense_df = box_defense.get_data_frames()[0]
# print(box_defense_df)

# Find a specific game.
# game = leaguegamefinder.LeagueGameFinder(player_or_team_abbreviation='P', team_id_nullable = '1612709932').get_data_frames()[0]
# print(game)

#stats = playercareerstats.PlayerCareerStats(per_mode36='PerGame', player_id='2544').get_data_frames()[0]
#print(stats)

# nba_guys = players.get_players()
# sorted_players = sorted(nba_guys, key=lambda player: player['id'])
# all_players_df = pd.DataFrame(sorted_players)
# print(all_players_df)

#roto = gamerotation.GameRotation(game_id='0022201228').get_data_frames()[0]
#print(roto)