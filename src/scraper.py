import json
import requests
from bs4 import BeautifulSoup

URL = 'https://www.espn.com/nba-summer-league/schedule'
page = requests.get(URL) # This line gets the HTML code from the given URL. 

soup = BeautifulSoup(page.content, "html.parser")
teams = soup.find_all("div", class_="matchTeams") # When inspecting the HTML of the 'matches' table, divided by className.

matches = []
for i in range(0, len(teams)-1, 2):
    # Get the plaintext of Home and Away teams.
    home_team = teams[i].find("span").text
    away_team = teams[i+1].find("span").text
    
    # Check if the teams are not 'TBD' before extracting the logos
    if home_team != 'TBD' and away_team != 'TBD':
        home_logo = teams[i].find("img")['src'] if teams[i].find("img") else None
        away_logo = teams[i+1].find("img")['src'] if teams[i+1].find("img") else None
        matches.append({
            "homeTeam": home_team, 
            "homeLogo": home_logo,
            "awayTeam": away_team, 
            "awayLogo": away_logo
        })

with open('matches.json', 'w') as f:
    json.dump(matches, f)