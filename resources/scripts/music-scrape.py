from selenium import webdriver
from string import ascii_uppercase
from bs4 import BeautifulSoup
import pandas as pd
import re

driver = webdriver.Chrome("/Users/anmolsaini/chromedriver_mac64/chromedriver")
albums_info = []
#url = "https://vgmdb.net/search?do=results&id=1061698&field=&"
#url = "https://vgmdb.net/search?do=results&id=1061698&field=&&page=5"
#url = "https://vgmdb.net/search?do=results&id=1064546&field=&&page=5"
url = "https://vgmdb.net/search?do=results&id=1064546&field=&"

next_page_exists = True
# page_num = 1
class_index = 1

while next_page_exists:
    driver.get(url)
    index_page = driver.page_source
    index_soup = BeautifulSoup(index_page, 'lxml')
    table_html = index_soup.find("td", class_="alt1")
    headings_html = table_html.find("tr")
    albums_headings_html = headings_html.next_sibling.next_sibling.find_next_siblings("tr")
    for album_heading_html in albums_headings_html:
        album_info = []
        if class_index % 2 == 1:
            class_name = "alt1"
        else:
            class_name = "alt2"
        class_index += 1
        album_heading_html_list = album_heading_html.find_all("td", class_=class_name)

        child_status_html = album_heading_html_list[1]
        child_status = child_status_html.find("img", title="Child album")
        if child_status != None:
            continue

        album_title_html = album_heading_html_list[2]
        #print(album_title_html.prettify())
        album_link = album_title_html.find('a', href=True)
        driver.get(album_link["href"])
        album_page = driver.page_source
        album_soup = BeautifulSoup(album_page, 'lxml')

        #---------
        right_column = album_soup.find("td", id="rightcolumn")
        album_stats_box = right_column.find("div", class_="smallfont")
        album_stats_box_list = album_stats_box.find_all("div", style="margin-bottom: 10px;")
        products_represented_box = album_stats_box_list[3]
        games_soup = BeautifulSoup(products_represented_box)
        games_text = games_soup.get_text(separator=', ')
        print(games_text)
        # print(products_represented_box.get_text(seperator=', '), end="\n")
        # games = re.sub(r' /.+?\n', ',', f"{products_represented_box.text.lstrip()[20:]}\n").strip("\n,")
        # print(games)
        #composer_en = re.sub(r' /.+?,', ',', f"{composer_html.text.strip()},").rstrip(",")
        #games = album_stats_box.find_all(class_="productname", lang="en")
        #print(album_stats_box.prettify())
        # games_list = []
        # for game in games:
        #     games_list.append(game.text)
        #     print(game.text)
        # print(games_list)
        # album_info.append(games_list)
        #---------

        album_title = album_soup.find(class_="albumtitle", lang="en")
        album_info.append(album_title.text)
        #print(album_title.text)

        tracklist_box = album_soup.find("span", class_="tl")
        if tracklist_box == None:
            continue
        tracks_info_list = tracklist_box.find_all("tr", class_="rolebit")
        tracks_list = []
        for track_info in tracks_info_list:
            track_info_list = track_info.find_all("td", class_="smallfont")
            track_name = track_info_list[1].text.strip()
            tracks_list.append(track_name)
            #print(track_name)
        album_info.append(tracks_list)

        credits_html_excess = album_soup.find_all("table", id="album_infobit_large")
        credits_html = credits_html_excess[1]
        #print(credits_html.prettify())
        composer_heading_html = credits_html.find("span", title="Composer")
        if composer_heading_html != None:
            #print(composer_html.prettify())
            composer_html = composer_heading_html.parent.parent.parent.next_sibling
            #print(composer_html.text.strip())
            #         composer_en = composer_html.text.split("/", 1)[0].strip()
            composer_en = re.sub(r' /.+?,', ',', f"{composer_html.text.strip()},").rstrip(",")
            #print(composer_en)
            #print(composer_en)
            album_info.append(composer_en)
            # Chanchacorin*, Ogeretsu Kun / おげれつくん*, Bunbun / ぶんぶん*, Ojalin*, Mari / まり*, YUKO*
            # Chanchacorin*, Ogeretsu Kun  Bunbun  Ojalin*, Mari  YUKO*
            # Chanchacorin*, Ogeretsu Kun, Bunbun, Ojalin*, Mari, YUKO*

        albums_info.append(album_info)
        print(album_info, end="\n")

    pages_html = index_soup.find("div", class_="pagenav")
    current_page = pages_html.find("td", class_="alt2")
    next_page = current_page.find_next_sibling("td", class_="alt1")
    if next_page == None:
        next_page_exists = False
        #continue
    else:
        next_page_link = next_page.find("a", href=True)
        #print(next_page_link)
        url = (f"https://vgmdb.net{next_page_link['href']}")
        #print(url)
        # page_num+=1
        # url = f"{url}&page={page_num}"
        #break


#print(album_info)
#print(album_heading_html_list)
driver.close()
