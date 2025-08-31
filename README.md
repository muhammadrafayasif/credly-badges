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

```yaml
name: Daily Badges

on:
  schedule:
    - cron: '0 12 * * *' # Runs daily at 12:00 UTC
  workflow_dispatch:       # Allow manual trigger

jobs:
  daily-badges:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Run Credly Badges Action
        uses: muhammadrafayasif/credly-badges@v1.0.0
        with:
          credly-username: "your-credly-username"
          output-path: "badges"

      - name: Commit and push badges
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add badges/
          git commit -m "Update Credly badges [skip ci]" || echo "No changes to commit"
          git push
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
