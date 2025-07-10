import camoufox

class ScraperManager:
    def __init__(self, config):
        self.config = config
        self.scrapers = []


    def add_scraper(self, scraper):
        self.scrapers.append(scraper)

