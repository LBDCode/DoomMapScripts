from bs4 import BeautifulSoup
import requests
import re


def getHurricaneData():
    url = "https://www.nhc.noaa.gov/gis/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    links = soup.select('a[href*="5day_latest"]')

    for link in links:
        print(url + link['href'])

    # first_table = soup.select_one("table:nth-of-type(1)")
    # atlantic_cells = first_table.select('tr:nth-of-type(3) td:nth-of-type(2)')
    # eastern_pacific_cells = first_table.select('tr:nth-of-type(3) td:nth-of-type(3)')
    # central_pacific_cells = first_table.select('tr:nth-of-type(3) td:nth-of-type(4)')
 
    # regions = [atlantic_cells, eastern_pacific_cells, central_pacific_cells]



getHurricaneData()