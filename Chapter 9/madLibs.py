# madLibs.py - reads a text file and lets the user add in their own text anywhere the words ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
import os, re
from pathlib import Path
# open a text file
original_input_text = open('.\inputText.txt').read()
def replacement(inputText):
    if not re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB',inputText):
        print(inputText)
        open('.\inputText.txt','w').write(inputText)
    for word in re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB',inputText):
        print("Enter a " + word.lower() + ':')
        replacement(req.sub(word,input(),inputText,1))
        break
replacement(inputText)
