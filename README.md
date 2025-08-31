# 🏅 Credly Badges GitHub Action

Automatically scrape your **Credly badges** and generate a neat SVG image grid that you can use in your GitHub profile README, portfolio, or website.  

---

## ✨ Features
- Scrapes all badges from a given **Credly username**  
- Generates an **SVG grid** of badges (embedded as base64)  
- Runs **daily** or on manual dispatch  
- Can be used as a **GitHub Action** or standalone script  

---

## 🚀 Usage

Add the following workflow to `.github/workflows/daily-badges.yml` in your repo:

>[!NOTE]
>The Action is not published on the market yet, so use muhammadrafayasif/credly-badges@main instead

```yaml
name: Daily Credly Badges

on:
  schedule:
    - cron: '0 12 * * *'  # runs daily at 12:00 UTC
  workflow_dispatch:       # manual trigger

jobs:
  fetch-badges:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v3

      - name: Fetch Credly Badges
        uses: muhammadrafayasif/credly-badges@v1.0.0
        with:
          credly-username: "muhammadrafayasif"
          output-path: "badges"
          
      - name: Commit updated badges
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add badges/
          git commit -m "chore: update Credly badges SVG [skip ci]" || echo "No changes to commit"
          git push
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
