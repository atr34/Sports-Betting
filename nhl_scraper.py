from bs4 import BeautifulSoup
import requests
import sys

def scrape_data_nhl(year):
    url = "https://www.hockey-reference.com/leagues/NHL_{}.html".format(year)
    print(url)
    # find and parse what we want from the website
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    teams = doc.find_all(class_="full_table")
    print('start')
    i = 1
    team_records = dict.fromkeys(['year' ,'name', 'gp', 'w', 'l', 'ol', 'pts', 'pts', 'gf', 'ga', 'srs', 'sos', 'rpt', 'rw', 'RgRec', 'RgPt'])
    for team in teams:
        print('Gathering data for team ', i)
        i+=1
    
if len(sys.argv) == 1:
    scrape_data_nhl('2022')
else:
    print('Hello')
    scrape_data_nhl(sys.argv[1])