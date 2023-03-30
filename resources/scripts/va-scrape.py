from selenium import webdriver
from string import ascii_uppercase
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/Users/anmolsaini/chromedriver_mac64/chromedriver")
#games_links = []
#data_df = pd.DataFrame(columns=['Game', 'Character', 'Voice Actor'])
games_info = []
for letter in ascii_uppercase:
    url = f"https://www.behindthevoiceactors.com/video-games/{letter}/"
    driver.get(url)
    #for
    letter_page = driver.page_source
    letter_soup = BeautifulSoup(letter_page, 'lxml')
    #print(letter_soup.prettify)
    letter_games_html = letter_soup.find("div", class_="credit_pics_container")
    #print(letter_games_html.prettify())
    games_details_html = letter_games_html.find_all("div", class_="browsee")
    #print(games_details_html)
    for game_details_html in games_details_html:
        # print(game_details_html, end="\n"*2)
        #game_info = []
        game_name = game_details_html.find('a', title=True)
        #print(game_name["title"])
        #game_info.append(game_name["title"])
        game_link = game_details_html.find('a', href=True)
        # games_links.append(games_link["href"])
        driver.get(game_link["href"])
        game_page = driver.page_source
        game_soup = BeautifulSoup(game_page, 'lxml')
        #print(game_soup.prettify())
        # game_cast_html = game_soup.find_all("div", class_="credit_pics_container") # this should find only one, but it's not
        game_cast_html_excess = game_soup.find_all("div", class_="credit_pics_container")
        game_cast_html = game_cast_html_excess[1]
        # print(game_cast_html) # wrong output because multiple classes with this name
        # print(game_cast_html)
        game_actor_character_html_list = game_cast_html.find_all("div", class_="credit_pic_float credit_pic_float_sidebyside")
        #print(game_actor_character_html_list)
        for game_actor_character_html in game_actor_character_html_list:
            game_info = []
            game_info.append(game_name["title"])
            #pass
            #print(game_actor_character_html, end="\n"*2)
            character_name = game_actor_character_html.find('a', title=True)
            #print(names[1]["title"])
            va_name = character_name.find_next_sibling('a', title=True)
            if (va_name == None):
                print(f"{game_name['title']}, {character_name['title']} has no va")
                continue
            game_info.append(character_name["title"])
            game_info.append(va_name["title"])
            #print(game_info, end="\n")
            games_info.append(game_info)
        # print(games_info, end="\n")
        # print("\n")
    #print(games_links)
data_df = pd.DataFrame(games_info, columns = ['Game', 'Character', 'Voice Actor'])
data_df.to_csv('va-dataset.csv', index=False)
    #exit()
driver.close()
