from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

# path specific to my system
driver = webdriver.Chrome("/Users/anmolsaini/chromedriver_mac64/chromedriver")
albums_info = []

# This url is valid for only a week from the creation date.
# The search parameters are listed below to make replication easier.
url = "https://vgmdb.net/search?do=results&id=1067741&field=&"

# Search Parameters
# publisher type -- Commercial, Doujin/Indie
# distribution type -- General
# release status -- No Status
# category -- Game
# classification -- Original Soundtrack
# sort by album titles

next_page_exists = True
class_index = 1

# continues looping as long as a next page can be found
while next_page_exists:
    driver.get(url)
    index_page = driver.page_source
    index_soup = BeautifulSoup(index_page, 'lxml')
    table_html = index_soup.find("td", class_="alt1")
    headings_html = table_html.find("tr")
    albums_headings_html = headings_html.next_sibling.next_sibling.find_next_siblings("tr")
    
    # loops for all albums on the current page
    for album_heading_html in albums_headings_html:
        album_info = []
        if class_index % 2 == 1:
            class_name = "alt1"
        else:
            class_name = "alt2"
        class_index += 1
        album_heading_html_list = album_heading_html.find_all("td", class_=class_name)

        # checks if the album is a child of another album, skipping it if so
        child_status_html = album_heading_html_list[1]
        child_status = child_status_html.find("img", title="Child album")
        if child_status != None:
            continue

        # gets the page for the album
        album_title_html = album_heading_html_list[2]
        album_link = album_title_html.find('a', href=True)
        driver.get(album_link["href"])
        album_page = driver.page_source
        album_soup = BeautifulSoup(album_page, 'lxml')

        # extracts the English names of games from which the album's music comes
        right_column = album_soup.find("td", id="rightcolumn")
        album_stats_box = right_column.find("div", class_="smallfont")
        album_stats_box_list = album_stats_box.find_all("div", style="margin-bottom: 10px;")
        if 3 < len(album_stats_box_list):
            products_represented_box = album_stats_box_list[3]
            for br in products_represented_box.select('br'):
                br.replace_with('\|/')
            games = re.sub(r' /.+?\|/', '\|/', f"{products_represented_box.text.strip()[24:]}\|/").rstrip("\|/")
            games_list = games.split("\|/")
            album_info.append(games_list)
        else:
            album_info.append("")

        # extracts the English name of the album itself
        album_title = album_soup.find(class_="albumtitle", lang="en")
        album_info.append(album_title.text)

        # extracts the English names of tracks in the album
        tracklist_box = album_soup.find("span", class_="tl")
        if tracklist_box == None:
            album_info.append("")
        else:
            tracks_info_list = tracklist_box.find_all("tr", class_="rolebit")
            tracks_list = []
            for track_info in tracks_info_list:
                track_info_list = track_info.find_all("td", class_="smallfont")
                track_name = track_info_list[1].text.strip()
                tracks_list.append(track_name)
            album_info.append(tracks_list)

        # extracts the English names of composers of the album's music
        credits_html_excess = album_soup.find_all("table", id="album_infobit_large")
        if 1 < len(credits_html_excess):
            credits_html = credits_html_excess[1]
            composer_heading_html = credits_html.find("span", title="Composer")
            if composer_heading_html != None:
                composer_html = composer_heading_html.parent.parent.parent.next_sibling
                composers_str = re.sub(r' /.+?,', ',', f"{composer_html.text.strip()},").rstrip(",")
                composers_list = composers_str.split(", ")
                album_info.append(composers_list)
            else:
                album_info.append("")
        else:
            album_info.append("")
        
        albums_info.append(album_info)

    # gets the link to the next page if it exists
    pages_html = index_soup.find("div", class_="pagenav")
    current_page = pages_html.find("td", class_="alt2")
    next_page = current_page.find_next_sibling("td", class_="alt1")
    if next_page == None:
        next_page_exists = False
    else:
        next_page_link = next_page.find("a", href=True)
        url = (f"https://vgmdb.net{next_page_link['href']}")

# puts the extracted data in a csv
data_df = pd.DataFrame(albums_info, columns = ['Games', 'Album', 'Tracks', 'Composers'])
data_df.to_csv('music_dataset.csv', index=False)
driver.close()
