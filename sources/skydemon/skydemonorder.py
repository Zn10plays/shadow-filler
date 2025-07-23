from scraper.scraper import BaseScraper
import re

regx = r'^(?:https?:\/\/)?skydemonorder\.com\/projects\/([\w-]+)(?:\/([\w-]+))?\/?.*$'

class SkydemonOrderScraper(BaseScraper):
    def __init__(self):
        super().__init__(name="SkydemonOrder", id=1, lang="en")

    def parse_url(self, url: str):
        match = re.match(regx, url)
        if match:
            project = match.group(1)
            chapter = match.group(2)
            return project, chapter
        return None, None

    def can_handle(self, url: str) -> bool:
        parsed = self.parse_url(url)
        return parsed[0] is not None

    def get_novel_info(self, url: str):
        # Implementation for fetching novel info
        pass

    def get_chapter_info(self, url: str):
        # Implementation for fetching chapter info
        pass
    
    def get_chapter_links(self, url: str):
        # Implementation for fetching chapter links
        pass