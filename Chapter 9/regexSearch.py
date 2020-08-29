# regexSearch.py - opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression, then prints the results to the screen.

import os, re
from pathlib import Path
# set the working directory to the specified search folder
os.chdir('./Chapter 9/regexSearch files')
print('Input a regular expression to search for:')
# collect a regular expression from the user
user_regex = str(input())
print('Search results:')
# iterate through each .txt file in the specified folder
for file in Path.cwd().glob('*.txt'):
# open each file in the folder
    text_file = open(file)
# search for the regex in the file and add each hit to a list
    results = re.findall(user_regex, text_file.read())
# if the list of results is not empty, print the file name and the list of matching results
    if results:
        print(os.path.basename(file) + ': ')
        for result in results:
            print(result)

