from scraper.scraper import BaseScraper
import re
from camoufox import AsyncCamoufox
from playwright_captcha.utils.camoufox_add_init_script.add_init_script import get_addon_path
import os
from playwright_captcha import CaptchaType, ClickSolver, FrameworkType
from utils.types.novels import NovelInfo, ChapterInfo, ChapterLinks, ChapterRef
from utils.proxies.manager import get_proxy
import asyncio

ADDON_PATH = get_addon_path()

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

    async def get_novel_info(self, url: str) -> NovelInfo:
        pass

    async def get_chapter_info(self, url: str) -> ChapterInfo:
        
        project, chapter = self.parse_url(url)
        if not project or not chapter:
            raise ValueError(f"Invalid URL: {url}")

        async with AsyncCamoufox(
            headless=True,
            geoip=True,
            humanize=True,
            i_know_what_im_doing=True,
            config={'forceScopeAccess': True},  # add this when creating Camoufox instance
            disable_coop=True,  # add this when creating Camoufox instance
    
            main_world_eval=True,  # 1. (only for camoufox) add this to use `add_init_script` temporary workaround
            addons=[os.path.abspath(ADDON_PATH)]
            # 2. (only for camoufox) add this to use `add_init_script` temporary workaround
        ) as browser:
            context = await browser.new_context()

            page = await context.new_page()
            await page.goto(url)

            framework = FrameworkType.CAMOUFOX
            async with ClickSolver(framework=framework, page=page) as solver:
                await page.goto(url, wait_until='networkidle')

                # solve the captcha
                await solver.solve_captcha(
                    captcha_container=page,
                    captcha_type=CaptchaType.CLOUDFLARE_INTERSTITIAL,
                    expected_content_selector="#chapter-body"
                )

            # Now we can extract the chapter content
            content_body = await page.query_selector_all('#chapter-body > p')

            chapter_content = []
            for paragraph in content_body:
                text = await paragraph.inner_text()
                chapter_content.append(text)

            chapter_content = "\n".join(chapter_content)
            
            title_elm = await page.query_selector_all('h1')

            if title_elm[0]:
                title = await title_elm[0].inner_text()
            else:
                title = "Unknown Title"

            match = re.search(r'\d+', title)
            if match:
                page_number = match.group()

            if not page_number:
                page_number = "-1"

            chapter_ref = ChapterRef(
                title=title,
                url=url,
                chapter_number=int(page_number)
            )

            # id don't matter will get overwritten in the database
            return ChapterInfo(
                id=int(page_number),
                ref=chapter_ref,
                content=chapter_content
            )

        pass    

    async def get_chapter_links(self, url: str) -> ChapterLinks:
        # Implementation for fetching chapter links
        pass