import os
from bs4 import BeautifulSoup
import requests

# Start a session
session = requests.Session()

# Define the login url
login_url = "https://www.streetfighter.com/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
# Define the payload (username and password)

payload = {"username": os.getenv("SF_USERNAME"), "password": os.getenv("SF_PASSWORD")}


# Post the payload to the site to log in
session.post(login_url, data=payload, headers=headers)

# Scrape the list of high MMR players
players_url = "https://www.streetfighter.com/6/buckler/ranking/master"
response = session.get(players_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the elements that contain the player IDs
player_elements = soup.find_all("div", class_="player-id")
print(player_elements)
# # For each player, navigate to their match history page and scrape the data
# for player_element in player_elements:
#     player_id = player_element.text
#     match_history_url = f"https://www.streetfighter.com/6/buckler/profile/{player_id}/battlelog/rank#profile_nav"
#     response = session.get(match_history_url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     # Find the elements that contain the match history data
#     match_elements = soup.find_all("div", class_="match-data")

#     # For each match, extract the player and character names
#     for match_element in match_elements:
#         player1 = match_element.find("div", class_="player1").text
#         player2 = match_element.find("div", class_="player2").text
#         character1 = match_element.find("div", class_="character1").text
#         character2 = match_element.find("div", class_="character2").text

#         print(player1, player2, character1, character2)
