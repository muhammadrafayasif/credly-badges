from playwright.sync_api import sync_playwright
import svgwrite
USERID = 'muhammadrafayasif'

def create_image_grid(image_urls, rows, cols, cell_size, output_file="grid.svg"):
    """
    Create an SVG grid of images from URLs.

    :param image_urls: List of image URLs to include in the grid
    :param rows: Number of rows in the grid
    :param cols: Number of columns in the grid
    :param cell_size: Tuple (width, height) of each grid cell
    :param output_file: Output SVG filename
    """
    dwg = svgwrite.Drawing(output_file, 
                           size=(cols * cell_size[0], rows * cell_size[1]))
    
    for idx, url in enumerate(image_urls):
        row = idx // cols
        col = idx % cols
        if row >= rows:
            break  # stop if more images than grid slots

        x = col * cell_size[0]
        y = row * cell_size[1]

        # Add image with given URL
        dwg.add(
            dwg.image(href=url, insert=(x, y), size=cell_size)
        )

    dwg.save()
    print(f"SVG saved as {output_file}")

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
