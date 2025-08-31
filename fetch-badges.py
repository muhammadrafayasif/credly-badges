from playwright.sync_api import sync_playwright
import svgwrite, requests, base64
USERID = 'muhammadrafayasif'

def url_to_data_uri(url):
    """
    Download an image from a URL and return it as a base64 data URI.
    """
    response = requests.get(url)
    response.raise_for_status()
    mime_type = response.headers.get("Content-Type", "image/png")  # fallback to PNG
    encoded = base64.b64encode(response.content).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"

def create_image_grid(image_urls, rows, cols, cell_size, output_file="grid.svg"):
    """
    Create a self-contained SVG grid of images (embedded as base64).
    """
    width, height = cols * cell_size[0], rows * cell_size[1]
    dwg = svgwrite.Drawing(output_file, size=(width, height))
    
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
    print(f"SVG saved as {output_file}. It's self-contained and works on GitHub.")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(java_script_enabled=True) 
    page = browser.new_page()
    page.goto(f'https://www.credly.com/users/{USERID}/badges#credly')
    page.wait_for_selector('.EarnedBadgeCardstyles__ImageContainer-fredly__sc-gsqjwh-0.dDMlBy', timeout=60000)
    badges = page.query_selector_all('.EarnedBadgeCardstyles__ImageContainer-fredly__sc-gsqjwh-0.dDMlBy')

    images = [i.get_attribute('src') for i in badges]
    for i in images:
        print(i)
    create_image_grid(images, 3, 4, (100, 100))

    browser.close()
