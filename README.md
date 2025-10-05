# 🏅 Credly Badges GitHub Action

Automatically scrape your **Credly badges** and generate a neat grid that you can use in your GitHub profile README.

---

## ✨ Features
- Scrapes all badges from a given **Credly username**  
- Dynamically updates the README of your profile to include all Credly badges
- Runs **daily** or on manual dispatch  
- Can be used as a **GitHub Action** or standalone script  

---

## 🚀 Usage

Add the following workflow to `.github/workflows/daily-badges.yml` in your repo:

>[!NOTE]
> Replace `credly-username` with your username from Credly

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
          credly-username: "[username]"
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
```
## 🖼️ Demonstration
<!-- START_CREDLY_BADGES -->
<a href="https://www.credly.com/badges/7806219c-f1a9-4335-bd83-92d7e7812dc3"><img src="https://images.credly.com/images/6eb08161-0425-4fc0-b66c-a1138dee7953/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/e8565dd7-0725-42cf-bd1d-6d82edda4651"><img src="https://images.credly.com/images/1dc40257-c856-4e6b-9a92-29be936a9e7c/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/438cfebe-6dc9-48ac-874b-be76337c39f6"><img src="https://images.credly.com/images/42ce4209-8839-431a-9046-f2ce2e72e04b/Coursera_20Data_20Science_20Professional_20Certificate.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/8ffd7d48-35e7-443a-a2dd-56da6d3d8b29"><img src="https://images.credly.com/images/169512d3-cef6-43e3-bec8-e6af2723a076/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/cb9141d9-4679-4c64-9f1a-e57e289fd59c"><img src="https://images.credly.com/images/56c60565-e945-4bcd-b8a6-9b2f43e1b0d9/Coursera_20Machine_20Learning_20with_20Python_20V2.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/12562254-ac2b-4f7c-a639-57345625b1fc"><img src="https://images.credly.com/images/9da3eedf-fda3-4e81-bb46-d174b4699bf1/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/2ac944b2-576b-4f3d-97d4-68ba8f5b4d3b"><img src="https://images.credly.com/images/950038fc-2519-4f79-8827-f71caf0f5095/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/e4f9b7ce-933a-460d-9548-8b27ce8c28ef"><img src="https://images.credly.com/images/f2573aac-d21c-483d-acda-afaa366b4f51/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/66aa6289-de27-4558-96ba-7df870534372"><img src="https://images.credly.com/images/46defa53-a922-47bd-94ea-b43488f5cd8a/Data_Science_Methodology_Foundational.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/157aad74-b9d9-4870-a20b-259e61d6b51e"><img src="https://images.credly.com/images/4dd14b9d-2750-43bc-a5f6-27970c0de0fa/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/c6822347-a593-4df6-95de-26622c3eca45"><img src="https://images.credly.com/images/40bee502-a5b3-4365-90e7-57eed5067594/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/bfa6fe18-08c1-4a66-be9b-b32e0dbfeb62"><img src="https://images.credly.com/images/1447954e-9923-4703-a647-eac80e5f0682/image.png" alt="Credly Badge" width="100"/></a>
<a href="https://www.credly.com/badges/dda8ec7a-abd0-459b-b750-2bb3d35998f8"><img src="https://images.credly.com/images/5fc2d535-e716-46c4-881a-f4822b8da0e5/Cognitive_Class_-_What_is_Data_Science.png" alt="Credly Badge" width="100"/></a>
<!-- END_CREDLY_BADGES -->
