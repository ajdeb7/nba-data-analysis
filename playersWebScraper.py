import requests
from bs4 import BeautifulSoup
import csv

def scrape_players():

    # Create structure of new csv for scraped data
    # Only run once
    """ header = ['Player', 'Team', 'Age', 'Experience', 'Height'] 

    # Write header as first row of csv
     with open('NbaStandings2019Dataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header) """


scrape_players()