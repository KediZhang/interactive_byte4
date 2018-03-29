

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
    

    with open('relation2.txt', encoding='utf-8', mode='w+') as f:
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

            lang_array = []
            for linklist in soup.find_all("div", {"class": "wikibase-listview"}):
                for span in linklist.div.find_all("span", {"class": "wikibase-sitelinkview-page"}):
                #print (mydivs)
                    lang = span.get("lang")
                    lang_array.append(lang)
                if not lang_array:
                    print("empty")
                else:
                    print (lang_array)
                    f.writelines(str(lang_array)+"\n")
            # https://en.wikipedia.org/wiki/

        f.close()


# def lang_relationship():
#     resp = requests.get(""""https://en.wikipedia.org/w/api.php?action=query&titles="""+ pagetile +"""&prop=langlinks""")
#     print(resp.status_code)   #  200
#     print(resp.json())

scraping()
#lang_relationship()