from shadow_db import Novel, Chapter
from camoufox_captcha import solve_captcha
from camoufox import AsyncCamoufox
import asyncio
import time
from scraper.manager import manager

async def main():
    
    # log time
    start_time = time.time()

    chapter_info = await manager.get_chapter_info('https://skydemonorder.com/projects/3801994495-return-of-the-mount-hua-sect/971-know-that-this-is-glory-kid-1')
    
    # print(chapter_info)
    print(chapter_info.ref.title)
    print(chapter_info.ref.chapter_number)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())