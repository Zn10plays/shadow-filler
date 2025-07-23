from utils.types.novels import NovelInfo, ChapterInfo, ChapterLinks
from pydantic import BaseModel

class Lang:
    en = 'en'
    ko = 'ko'
    ja = 'ja'
    zh = 'zh'
    es = 'es'
    fr = 'fr'
    de = 'de'
    it = 'it'
    pt = 'pt'
    ru = 'ru'

class BaseScraper:
    def __init__(self, name: str, id: int, lang: Lang = Lang.en):
        self.name = name
        self.id = id
        self.lang = lang

    def can_handle(self, url: str) -> bool:
        raise NotImplementedError

    async def get_novel_info(self, url: str) -> NovelInfo:
        raise NotImplementedError

    async def get_chapter_info(self, url: str) -> ChapterInfo:
        raise NotImplementedError

    async def get_chapter_links(self, url: str) -> ChapterLinks:
        raise NotImplementedError