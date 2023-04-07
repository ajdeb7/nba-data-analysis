import requests
from bs4 import BeautifulSoup
import csv

def scrape_team_records():

    # Create structure of new csv for scraped data
    # Only run once
    """ header = ['Team Name', 'Wins', 'Losses', 'W/L%'] 

    # Write header as first row of csv
     with open('NbaStandings2019Dataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header) """

    url = "https://www.basketball-reference.com/leagues/NBA_2023.html"

    # Make a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the team records
    west_table = soup.find('table', {'id': 'confs_standings_W'})
    east_table = soup.find('table', {'id': 'confs_standings_E'})

    # Get the rows from the table
    west_rows = west_table.find_all('tr')
    east_rows = east_table.find_all('tr')


    # Loop through each row and extract the team name, win-loss record, and other data
    for row in west_rows[1:]:
        team_cell = row.find_all('th')
        team_name = team_cell[0].text.strip()
        cells = row.find_all('td')
        wins = cells[0].text.strip()
        losses = int(cells[1].text.strip())
        win_loss_pct = float(cells[2].text.strip())
        data = [team_name, wins, losses, "%.3f" % win_loss_pct]
        with open('nbaStandings.csv', 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)



    # Loop through each row and extract the team name, win-loss record, and other data
    for row in east_rows[1:]:
        team_cell = row.find_all('th')
        team_name = team_cell[0].text.strip()
        cells = row.find_all('td')
        wins = cells[0].text.strip()
        losses = int(cells[1].text.strip())
        win_loss_pct = float(cells[2].text.strip())
        data = [team_name, wins, losses, "%.3f" % win_loss_pct]
        with open('nbaStandings.csv', 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

        # Print the data writing to csv
        # print(data)

scrape_team_records()


# Insert scraped data to csv
    #writer.writerow(data)