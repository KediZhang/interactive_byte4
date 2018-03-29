

# https://meta.wikimedia.org/wiki/List_of_articles_every_Wikipedia_should_have

import requests
from bs4 import BeautifulSoup
import os
from os import path
import shutil
import string
import codecs
import numpy as np


#def scraping_list():

def scraping():
    #Here we create dicts and lists
    LINK = []

    with open('test.txt', encoding='utf-8', mode='w+') as f:
    #state the index page we want to scrape
        site = "https://meta.wikimedia.org/wiki/List_of_articles_every_Wikipedia_should_have"
        #Scrape the website.
        get_web = requests.get(site)
        text_con = get_web.text
        soup = BeautifulSoup(text_con, 'html.parser')
        #Read html contents and create dic where key is title, value is the link

        for link in soup.find_all('a'):
            link_str = link.get('href')
            if str(link_str).startswith("https://www.wikidata.org/wiki/Q"):
                LINK.append(str(link_str))
    
        for link in LINK:
            site = link
            #Scrape the website.
            get_web = requests.get(site)
            text_con = get_web.text
            soup = BeautifulSoup(text_con, 'html.parser')

            mydivs = soup.findAll("span", {"class": "wikibase-title-label"})
            pagetitle = str(mydivs).split(">")[1]
            pagetitle = str(pagetitle).split("<")[0]
            print (pagetitle)
            f.writelines(pagetitle+"\n")
            # https://en.wikipedia.org/wiki/

        f.close() 


def lang_relationship():
    resp = requests.get(""""https://en.wikipedia.org/w/api.php?action=query&titles="""+ pagetile +"""&prop=langlinks""")
    print(resp.status_code)   #  200
    print(resp.json())

scraping()
lang_relationship()