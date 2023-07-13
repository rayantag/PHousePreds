from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog, leaguedashptteamdefend, boxscoredefensive, leaguegamefinder, boxscorematchups
from nba_api.stats.endpoints import defensehub, draftboard, drafthistory, playerawards, playercareerstats, gamerotation, playerindex
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from rapidfuzz import fuzz, process
import requests
import json

# Balldontlie API tests.

#url = "https://www.balldontlie.io/api/v1/players"
statsURL = "https://www.balldontlie.io/api/v1/stats?seasons[]=2022&player_ids[]=237&postseason=true"
#bronURL = "https://www.balldontlie.io/api/v1/players/237"

response = requests.get(statsURL)
data = response.json()
for dot in data["data"]:
    print (dot["pts"], dot["reb"], dot["ast"])


# actives = players.get_active_players()

# name_list = [active_player['full_name'] for active_player in actives]

# Fetch team defensive stats for a season

# input = 'shasdfai gilgeous-alexander'

# selected = process.extractOne(input, name_list, scorer=fuzz.WRatio)
# print(selected[0])

# input = 'Pole'
# plays = players.find_players_by_full_name(input)
# if not plays:
#     print("Error!")
# print(plays)
#play_id = plays[0]['id']
#print(play_id)

# p = playerindex.PlayerIndex(season="2022-23")
# p_df = p.get_data_frames()[0]
# player_row = p_df[p_df['PERSON_ID'] == play_id]
# vals = [player_row['PTS'].values[0], player_row['REB'].values[0], player_row['AST'].values[0]]
# print(vals)

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