#! python3
# openLinks.py - opens all links in a text document in their own browser tabs

import webbrowser,os,sys,re
from pathlib import Path

# get a txt file path from the command line
try:
    file_path = sys.argv[1]
except:
    print('openLinks requires a file path in the first argument position')      
# validate the path
if os.path.exists(file_path):
    # open and read a txt file
    url_file_content = open(file_path).read()
    # scan it for URLs using a regex
    url_list = re.findall('[https://]*[www\.]*\w+\.[a-z]+',url_file_content)
    # iterate through each item in the list of URLs and open a new tab for each
    for url in url_list:
        webbrowser.open(url)
