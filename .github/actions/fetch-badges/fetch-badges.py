import math, os, sys
from playwright.sync_api import sync_playwright
import svgwrite, requests, base64

def url_to_data_uri(url):
    """
    Download an image from a URL and return it as a base64 data URI.
    """
    response = requests.get(url)
    response.raise_for_status()
    mime_type = response.headers.get("Content-Type", "image/png")  # fallback to PNG
    encoded = base64.b64encode(response.content).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

def create_image_grid(image_urls, rows, cols, cell_size, output_folder="badges", output_file="grid.svg"):
    """
    Create a self-contained SVG grid of images (embedded as base64).
    """
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, output_file)
    width, height = cols * cell_size[0], rows * cell_size[1]
    dwg = svgwrite.Drawing(output_path, size=(width, height))

    dwg.add(dwg.rect(insert=(0, 0), size=(width, height), fill="white"))
    
    for idx, url in enumerate(image_urls):
        row = idx // cols
        col = idx % cols
        if row >= rows:
            break  # stop if more images than grid slots

        x = col * cell_size[0]
        y = row * cell_size[1]

        data_uri = url_to_data_uri(url)

        # Add the image as a base64 data URI
        dwg.add(
            dwg.image(href=data_uri, insert=(x, y), size=cell_size)
        )

    dwg.save()
    print(f"SVG saved as {output_path}.")

def main(username, output_folder):
    repo_root = os.getcwd()
    full_output_path = os.path.join(repo_root, output_folder)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f'https://www.credly.com/users/{username}/badges#credly')
        page.wait_for_selector('.EarnedBadgeCardstyles__ImageContainer-fredly__sc-gsqjwh-0.dDMlBy', timeout=60000)
        badges = page.query_selector_all('.EarnedBadgeCardstyles__ImageContainer-fredly__sc-gsqjwh-0.dDMlBy')

        images = [i.get_attribute('src') for i in badges]
        
        rows = math.ceil(len(images) / 4)
        columns = 4

        create_image_grid(images, rows, columns, (100, 100), full_output_path)

        browser.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("Usage: python fetch-badges.py <credly-username> [output_path]")
        sys.exit(1)

    username = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "badges"
    main(username, output_path)