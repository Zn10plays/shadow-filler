
from camoufox.sync_api import Camoufox
from shadow_db import Novel, Chapter

def main():
    novel = Novel.get(1)

    url = novel.url

    with Camoufox() as browser:
        page = browser.new_page()
        page.goto(url)

        
    pass

if __name__ == "__main__":
    main()