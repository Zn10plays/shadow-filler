from pydantic import BaseModel

class NovelRef(BaseModel):
    id: int
    title: str
    url: str

class NovelInfo(BaseModel):
    ref: NovelRef
    summary: str
    total_chapters: int
    last_updated: str
    cover_image: str|None = None

class ChapterRef(BaseModel):
    title: str
    url: str
    chapter_number: int

class ChapterInfo(BaseModel):
    id: int
    ref: ChapterRef
    content: str

class ChapterLinks(BaseModel):
    refrences: list[ChapterRef] = []
    novelref: NovelRef = None
