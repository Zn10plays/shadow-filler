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
    cover_image: any = None

class ChapterInfo(BaseModel):
    id: int
    title: str
    url: str
    chapter_number: int
    content: str = None  # Content can be optional if not fetched immediately