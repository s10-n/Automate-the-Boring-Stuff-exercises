#! python3
# downloadXkcd.py - downloads every single XKCD comic
import requests, os, bs4
url = 'https://xkcd.com' # starting URL
os.makedirs('xkcd',exist_ok=True) # store comics in an 'xkcd' folder
while not url.endswith('#'):
    # todo: download the page
    # todo: find the URL of the comic image
    # todo: download the image
    # todo: save the image to /xkcd
    # todo: get the 'Prev' button URL
print('Done.')
