import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# This scraper uses a blend of Selenium webdriver and Beautifulsoup to get summer league team names and logos. 
# Beautifulsoup is simpler than Selenium, but it could not be used to get the team logos because their static 
# HTML has urls encoded in base64 (for faster loading). Selenium is an interactive web scraper, so it actually 
# loads the webpage (causing the JavaScript to render), and then performing its actions. Thus, Selenium could have
# been used for this whole script, but just for practice both programs have been included.

currURL = "https://www.espn.com/nba-summer-league/schedule"

def getTeamsAndLogos(schedule_webpage):
    chrome_options = Options()

    # New browser session + headless mode to prevent browser from prematurely closing.
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Get rendered source code from desired webpage, close session after.
    driver.get(schedule_webpage)
    source_code = driver.page_source
    driver.quit()

    # Initialize a BeautifulSoup object to parse HTML code.
    soup = BeautifulSoup(source_code, 'html.parser')

    # Find divs with specified class. This depends on HTML structure when webpage is inspected.
    teams = soup.find_all('div', {'class': 'matchTeams'})

    matches = []
    for i in range(0, len(teams)-1, 2):
        # Get the plaintext of Home and Away teams.
        home_team = teams[i].find("span").text
        away_team = teams[i+1].find("span").text
        
        # Check if the teams are not 'TBD' before extracting the logos.
        if home_team != 'TBD' and away_team != 'TBD':
            home_logo = teams[i].find("img")['src'] if teams[i].find("img") else None
            away_logo = teams[i+1].find("img")['src'] if teams[i+1].find("img") else None
            matches.append({
                "homeTeam": home_team, 
                "homeLogo": home_logo,
                "awayTeam": away_team, 
                "awayLogo": away_logo
            })

    # Save to a JSON, which will be sent to client-side app.
    with open('matches.json', 'w') as f:
        json.dump(matches, f)


# TODO: fix this method to get top-performing players.

performURL = "https://www.nba.com/2023-summer-league-vegas-player-stats"
def getPerformers(perform_webpage):

    # Set up chrome options and webdriver in headless mode, same as before.
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(perform_webpage)

    # Now tried to wait so that the JavaScript could render the table before inspecting HTML. Got a TimeOutError, which means that 
    # the className was not found. The className provided could be wrong, however.
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Crom_body__UYOcU"))
        )
    finally:
        driver.quit()

    print(driver.page_source)
   
if __name__ == "__main__":
    getTeamsAndLogos(currURL)
    # getPerformers(performURL)