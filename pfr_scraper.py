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
