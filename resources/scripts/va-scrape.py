from selenium import webdriver
from string import ascii_uppercase
from bs4 import BeautifulSoup
import pandas as pd

games_info = []

# function to scrape the website for games that have names starting with the given letter
def scrape_page(driver, letter):
    url = f"https://www.behindthevoiceactors.com/video-games/{letter}/"
    driver.get(url)
    letter_page = driver.page_source
    letter_soup = BeautifulSoup(letter_page, 'lxml')
    letter_games_html = letter_soup.find("div", class_="credit_pics_container")
    games_details_html = letter_games_html.find_all("div", class_="browsee")

    # loops for each game starting with the given letter
    for game_details_html in games_details_html:
        game_name = game_details_html.find('a', title=True)
        game_link = game_details_html.find('a', href=True)
        driver.get(game_link["href"])
        game_page = driver.page_source
        game_soup = BeautifulSoup(game_page, 'lxml')
        game_cast_html_excess = game_soup.find_all("div", class_="credit_pics_container")
        game_cast_html = game_cast_html_excess[1]
        game_actor_character_html_list = game_cast_html.find_all("div", class_="credit_pic_float credit_pic_float_sidebyside")

        # loops for each voice actor and character pair in the game
        for game_actor_character_html in game_actor_character_html_list:
            game_info = []
            game_info.append(game_name["title"])
            character_name = game_actor_character_html.find('a', title=True)
            game_info.append(character_name["title"])
            va_name = character_name.find_next_sibling('a', title=True)
            if (va_name != None):
                game_info.append(va_name["title"])

            games_info.append(game_info)

# sets up the webdriver with an adblocker 
chop = webdriver.ChromeOptions()
# these paths are specific to my system
chop.add_extension("/Users/anmolsaini/extension_2_5_9_0.crx")
driver = webdriver.Chrome("/Users/anmolsaini/chromedriver_mac64/chromedriver", options = chop)

# scrapes the website for games starting with each letter and other symbols
scrape_page(driver, "$")
for letter in ascii_uppercase:
    scrape_page(driver, letter)
    
# puts the extracted data in a csv
data_df = pd.DataFrame(games_info, columns = ['Game', 'Character', 'Voice Actor'])
data_df.to_csv('va-dataset.csv', index=False)
driver.close()
