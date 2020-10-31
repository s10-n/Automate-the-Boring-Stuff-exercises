#! python3
# webComicDownloader.py - checks the websites of several web comics and automatically downloads the images if the comic was updated since the program’s last visit

import requests,os,bs4,re
from pathlib import Path

web_comics = [{'name':'xkcd',
               'homepage_url':'https://xkcd.com/',
               'css_selector':'img[srcset^="//imgs.xkcd.com/comics/"]'},
              {'name':'Buttersafe',
               'homepage_url':'https://www.buttersafe.com/',
              'css_selector':'img[src^="https://www.buttersafe.com/comics/"]'},
              {'name':'Savage Chickens',
               'homepage_url':'https://www.savagechickens.com/',
               'css_selector':'div.entry_content img'}]

# avoid any sort of bot filtering by including these headers
headers = {'User-Agent':"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}

for web_comic in web_comics:

    # create a folder for the comic if it doesn't exist already
    folder_path = f"./web comics/{web_comic['name']}/"
    os.makedirs(folder_path,exist_ok = True)

    # download the comic's homepage
    homepage = requests.get(web_comic['homepage_url'],headers=headers)
    homepage.raise_for_status()
    homepage_soup = bs4.BeautifulSoup(homepage.text,'html.parser')

    # get the most recent comic image and its URL using the designated selector
    image_element = homepage_soup.select(web_comic['css_selector'])
    image_url = image_element[0].attrs['src']

    # add 'http' if missing
    if not image_url.startswith('http'):
        image_url = 'http:' + image_url

    # download the image 
    image_filename = Path(image_url).name
    if image_filename not in os.listdir(folder_path):
        image = requests.get(image_url)
        image_file = open(os.path.join(folder_path,image_filename),'wb')
        for chunk in image.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        print(f"Successfully downloaded {image_filename} from {web_comic['name']}...")
