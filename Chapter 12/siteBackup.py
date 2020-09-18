#! python3
# siteBackup.py - backs up a website by following all of its links
import requests, os, bs4, re
from pathlib import Path

directory_name = input('Print the name of the folder you would like to store the website in: ')
os.makedirs(directory_name,exist_ok=True) # create the named directory
print('Created directory ' + str(Path.cwd()) + '/' +  directory_name)
def page_backup(url):
    # download the page and create a path
    page = requests.get(url)
    page.raise_for_status()
    page_file_path = os.path.join(directory_name,os.path.basename(url))
    # save the page to the directory if it doesn't exist yet
    if not os.path.exists(page_file_path):
        page_file = open(page_file_path,'wb')
        for chunk in page.iter_content(100000):
            page_file.write(chunk)
        page_file.close()
        print('Successfully saved ' + os.path.basename(url))
    # create a soup of the page and get all the links out of it
    pageSoup = bs4.BeautifulSoup(page.text, 'html.parser')
    list_of_urls = []
    # visit each link and call page_backup recursively
    for link in list(set(pageSoup.find_all('a'))):
        if link.get('href') not in list_of_urls and not re.search('https://|http://|mailto|#',link.get('href')):
            list_of_urls.append(link.get('href'))
    for url in list_of_urls:
        if not os.path.exists(os.path.join(directory_name,url)):
            page_backup(initial_url + '/' + url)

initial_url = input('Insert the url of the website you would like to back up: ')
if not re.search('^https://|^http://',initial_url):
    initial_url = 'http://' + initial_url
page_backup(initial_url)
