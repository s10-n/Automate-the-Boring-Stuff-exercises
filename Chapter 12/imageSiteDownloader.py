#! python3
# imageSiteDownloader.py - searches for the string passed to it on Imgur and then downloads all the resulting images

from selenium import webdriver
import os,requests
from pathlib import Path

def image_site_downloader(search_term):
  
    # open the Imgur search page for the search term in Firefox
    browser = webdriver.Firefox()
    browser.get('https://imgur.com/search?q=' + search_term)

    # find all of the image thumbnails on the search page and get their URLs
    # note that image URLs on the search page have a 'b' in them that denotes their status as thumbnails
    result_posts = browser.find_elements_by_css_selector('[src$="b.jpg"]')

    # count the number of posts found and exit program if 0
    if not len(result_posts):
        print('0 results found for "' + search_term + '" on Imgur.')
    else:
        print(str(len(result_posts)) + ' results found for "' + search_term + '" on Imgur.')

        # create a directory for the search term in the current working directory
        os.makedirs(search_term,exist_ok=True)

        # remove the 'b' from each thumbnail URL to get the full size image's URL
        for thumbnail in result_posts:
            split_image_url = thumbnail.get_attribute('src').split('b.')
            image_url = '.'.join(split_image_url)

            # download the image and save it locally
            online_image_file = requests.get(image_url)
            online_image_file.raise_for_status()
            local_image_path = os.path.join(search_term,os.path.basename(image_url))
            local_image_file = open(local_image_path,'wb')
            for chunk in online_image_file.iter_content(100000):
                local_image_file.write(chunk)

            # notify the user that the file has been saved
            print(os.path.basename(image_url) + ' saved to ' + str(os.path.join(Path.cwd(),search_term)))

            # close the local image file
            local_image_file.close() 

image_site_downloader(input('Type a search term: '))
