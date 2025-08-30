from playwright.sync_api import sync_playwright
import time
import json

USERID = 'muhammadrafayasif'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(java_script_enabled=True) 
    page = browser.new_page()
    page.goto(f'https://www.credly.com/users/{USERID}/badges#credly')
    page.wait_for_selector('.Typographystyles__Container-fredly__sc-1jldzrm-0.mWuVU.EarnedBadgeCardstyles__BadgeNameText-fredly__sc-gsqjwh-7.hqrelZ', timeout=60000)
    badges = page.query_selector_all('.Typographystyles__Container-fredly__sc-1jldzrm-0.mWuVU.EarnedBadgeCardstyles__BadgeNameText-fredly__sc-gsqjwh-7.hqrelZ')
    for badge in badges:
        print(badge.inner_html())
    browser.close()