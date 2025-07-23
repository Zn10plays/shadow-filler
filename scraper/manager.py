from scraper.scraper import BaseScraper
from utils.types.novels import NovelInfo, ChapterInfo, ChapterLinks
from sources.skydemon.skydemonorder import SkydemonOrderScraper

class ScraperManager:
    def __init__(self, config=None):
        self.config = config
        self.scrapers: list[BaseScraper] = []


    def add_scraper(self, scraper: BaseScraper):
        self.scrapers.append(scraper)

    def can_handle(self, url: str) -> int:
        for scraper in self.scrapers:
            if scraper.can_handle(url):
                return scraper.id
        return -1
    
    def get_scraper(self, id: int) -> BaseScraper:
        for scraper in self.scrapers:
            if scraper.id == id:
                return scraper
        raise ValueError(f"No scraper found with id: {id}")
    
    async def get_chapter_info(self, url: str) -> ChapterInfo:
        scraper_id = self.can_handle(url)
        if scraper_id == -1:
            raise ValueError(f"No scraper can handle the URL: {url}")
        
        scraper = self.get_scraper(scraper_id)
        return await scraper.get_chapter_info(url)

    async def get_novel_info(self, url: str) -> NovelInfo:
        scraper_id = self.can_handle(url)
        if scraper_id == -1:
            raise ValueError(f"No scraper can handle the URL: {url}")
        
        scraper = self.get_scraper(scraper_id)
        return await scraper.get_novel_info(url)
    
    async def get_chapter_links(self, url: str) -> ChapterLinks:
        scraper_id = self.can_handle(url)
        if scraper_id == -1:
            raise ValueError(f"No scraper can handle the URL: {url}")
        
        scraper = self.get_scraper(scraper_id)
        return await scraper.get_chapter_links(url)
    
manager = ScraperManager()
manager.add_scraper(SkydemonOrderScraper())  # Add your scrapers here