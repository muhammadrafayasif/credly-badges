import sys, re
from pathlib import Path
from playwright.sync_api import sync_playwright

def replace_section(text, start_tag, end_tag, new_content):
    pattern = re.compile(
        f"{re.escape(start_tag)}(.*?){re.escape(end_tag)}",
        re.DOTALL
    )
    replacement = f"{start_tag}\n{new_content.strip()}\n{end_tag}"
    return re.sub(pattern, replacement, text)

def main(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'https://www.credly.com/users/{username}/badges#credly')
        page.wait_for_selector('.EarnedBadgeCardstyles__ImageContainer-fredly__sc-gsqjwh-0.dDMlBy', timeout=60000)
        badges = page.query_selector_all('.EarnedBadgeCardstyles__ImageContainer-fredly__sc-gsqjwh-0.dDMlBy')
        links = page.query_selector_all('.Cardstyles__StyledContainer-fredly__sc-1yaakoz-0.fRJHRP.EarnedBadgeCardstyles__StyledCard-fredly__sc-gsqjwh-1.jwtiVz')

        images = [i.get_attribute('src') for i in badges]
        urls = [i.get_attribute('href') for i in links]
        
        README_PATH = Path("README.md")
        readme = README_PATH.read_text(encoding="utf-8")

        START_TAG = "<!-- START_CREDLY_BADGES -->"
        END_TAG = "<!-- END_CREDLY_BADGES -->"

        content = str()
        for n, i in enumerate(images):
            content+=f"<a href=\"https://wsrv.nl/?url=https://www.credly.com{urls[n]}\"><img src=\"{i}\" alt=\"Credly Badge\" width=\"100\"/></a>\n"
        
        updated = replace_section(readme, START_TAG, END_TAG, content)

        README_PATH.write_text(updated, encoding="utf-8")
        browser.close()

if __name__=='__main__':
    if len(sys.argv) < 1:
        print("Usage: python fetch-badges.py <credly-username>")
        sys.exit(1)

    username = sys.argv[1]
    main(username)