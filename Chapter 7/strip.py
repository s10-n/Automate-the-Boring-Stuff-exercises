# strip.py
# takes a string and a characters and removes the characters from the beginning and end of the string

import re

def my_strip(string, stripped=' '):
    print(re.sub(stripped, '', string))