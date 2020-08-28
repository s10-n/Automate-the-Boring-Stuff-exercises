# madLibs.py - reads a text file and lets the user add in their own text anywhere the words ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
import os, re
from pathlib import Path
# open a text file
#os.chdir(path(r'.\Chapter 9'))
#print(Path.cwd())
inputText = open('.\inputText.txt').read()
# find all instances of the words to be replaced
#print(re.sub(r'ADJECTIVE|NOUN|ADVERB|VERB',"shart",inputText))
def replacement(inputText):
    for word in re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB',inputText):
        print("Enter a " + word.lower() + ':')
        edited_text = re.sub(word,input(),inputText,1)
        print(edited_text)
        replacement(edited_text)
#    inputText.replace(word, "shart")
replacement(inputText)
#    re.sub(r'ADJECTIVE', input(), inputText)
# for each word to be replaced, prompt the user to replace them
# when every placeholder word has been replaced, print the story and write it to a new text file
#print(inputText)
