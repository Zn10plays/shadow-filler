from types.novels import NovelInfo, ChapterInfo

class BaseScraper:
    def can_handle(self, url: str) -> bool:
        raise NotImplementedError

    def get_novel_info(self, url: str) -> NovelInfo:
        raise NotImplementedError

    def get_chapter_info(self, url: str) -> ChapterInfo:
        raise NotImplementedError