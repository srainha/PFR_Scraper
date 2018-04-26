import re
import csv
import time
import itertools
from bs4 import BeautifulSoup
from urllib.request import urlopen


class PfrScraper:
    """
    A class for scraping NFL team data from PFR.
    """

    rawHTML = 'temp/raw.htm'
    tempHTML = 'temp/temp.htm'
    prettyHTML = 'temp/pretty.htm'
    resultPath = 'data/teams/'
    SOURCE = 'http://www.pro-football-reference.com/teams/'
    tableNames = ['Rankings', 'GameResults', 'Passing', 'Scrimmage',
                  'Returning', 'Kicking', 'Defense', 'Scoring', 'TDsFor',
                  'TDsAgainst']

    def __init__(self, team='ram', year=2016, table='GameResults'):
        self.year = year
        self.team = team
        self.table = table

    def getHTML(self):
        site = self.SOURCE + self.team + '/' + str(self.year) + '.htm'
        file = open(self.rawHTML, 'w')
        file.write(urlopen(site).read().decode("utf-8"))
        file.close()

    def stripComments(self):
        tags = re.compile("<!--\n|-->\n")
        with open(self.rawHTML, 'r') as rawFile, open(self.tempHTML, 'w+') as tempFile:
            for line in rawFile:
                if not (tags.match(line)):
                    tempFile.write(line)

