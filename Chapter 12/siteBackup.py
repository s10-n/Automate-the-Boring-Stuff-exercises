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
    # create a soup of the page and get all the links out of it
    pageSoup = bs4.BeautifulSoup(page.text, 'html.parser')
    list_of_urls = []
    for link in list(set(pageSoup.find_all('a'))):
        if link.get('href') not in list_of_urls and not re.search('https://',link.get('href')):
            list_of_urls.append(link.get('href'))
    print(list_of_urls)

page_backup(input('Insert the url of the website you would like to back up: '))
