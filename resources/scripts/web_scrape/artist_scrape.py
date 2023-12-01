from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# initial setup
driver = webdriver.Chrome("/Users/anmolsaini/chromedriver_mac64/chromedriver")
url = "https://www.creativeuncut.com/game-art-galleries.html"
driver.get(url)
index_page = driver.page_source
index_soup = BeautifulSoup(index_page, 'lxml')
games_info = []

# gets all the games
letter_headers_html = index_soup.find_all("div", class_="agj")
start_letter = letter_headers_html[1]
game_titles_html = start_letter.find_next_siblings("div", class_="ag")

# loops for each game, extracting the game's name and artists
for game_title_html in game_titles_html:
    game_info = []
    game_link = game_title_html.find('a', href=True)
    driver.get(f"https://www.creativeuncut.com/{game_link['href']}")
    game_page = driver.page_source
    game_soup = BeautifulSoup(game_page, 'lxml')
    game_info_box = game_soup.find("div", id="game_info")
    game_name = game_info_box.find("h1")
    game_info.append(game_name.text[:-4])
    game_artists = game_info_box.find_all("div", class_="gi_d3")
    game_info.append(game_artists[1].text)
    games_info.append(game_info)

# puts the extracted data in a csv
data_df = pd.DataFrame(games_info, columns = ['Game', 'Artists'])
data_df.to_csv('artist_dataset.csv', index=False)
driver.close()