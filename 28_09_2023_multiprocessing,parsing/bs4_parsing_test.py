import requests
from bs4 import BeautifulSoup

#
# html = """
# <html>
#     <body>
#         <p>Hello, world!</p>
#     </body>
# </html>
# """
# soup = BeautifulSoup(html, 'html.parser')
#
# print(soup.p.text)
##

# html = "<ul><li>Item 1</li><li>Item 2</li></ul>"
# soup = BeautifulSoup(html, 'html.parser')
#
# items = soup.find_all('li')
# for item in items:
#     print(item.text)
###############

def fetch_and_save_html(url, filename):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.content
            with open(filename, "wb") as file:
                file.write(html_content)
            print(f"Saved HTML from {url} to {filename}")
        else:
            print(f"Error: {response.status_code} - Unable to fetch HTML from {url}")
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")


url = 'https://unsplash.com/'


response = requests.get(url)
html = response.text
# print(html)

soup = BeautifulSoup(html, 'html.parser')

image_tags = soup.find_all('img')

for index, img_tag in enumerate(image_tags):
    try:
        img_srcset = img_tag['srcset']
        img_src = img_srcset.split()[4]
    except:
        continue

    if img_src:
        # suffix = ''
        #
        # if img_src.endswith('.gif'):
        #     suffix = '.gif'
        # elif img_src.endswith('.jpg'):
        #     suffix = '.jpg'
        # elif img_src.endswith('.png'):
        #     suffix = '.png'
        # else:
        #     continue

        fetch_and_save_html(img_src, f'./pictures/pic_{index}.avif')



