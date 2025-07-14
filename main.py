from shadow_db import Novel, Chapter
from camoufox_captcha import solve_captcha
from camoufox import AsyncCamoufox
import asyncio
import os
import dotenv

dotenv.load_dotenv()

WEBRTC_IPV6_PROXY = os.getenv("WEBRTC_IPV6_PROXY")


async def main():
    novel = Novel.get(1)

    url = novel.url

    async with AsyncCamoufox(
        headless=True,
        geoip=True,
        humanize=True,
        i_know_what_im_doing=True,
        config={'forceScopeAccess': True,
                'webrtc:ipv6': WEBRTC_IPV6_PROXY},  # add this when creating Camoufox instance
        disable_coop=True  # add this when creating Camoufox instance
    ) as browser:
        page = await browser.new_page()

        # navigate to a site with Cloudflare protection
        await page.goto(url)

        # solve using solve_captcha
        success = await solve_captcha(page, captcha_type='cloudflare', challenge_type='interstitial', expected_content_selector='.content')
        if not success:
            return print("Failed to solve captcha challenge")

        print("Successfully solved captcha challenge!")
        
        await page.screenshot(path='type shit.png')


    

if __name__ == "__main__":
    asyncio.run(main())