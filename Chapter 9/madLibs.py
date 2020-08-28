# madLibs.py - reads a text file and lets the user add in their own text anywhere the words ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
import os, re
from pathlib import Path
# open the inputText file
original_input_text = open('inputText.txt').read()
# define the function that replaces the text recursively
def replacement(inputText):
# if any of the words to be replaced are not found in the input text, the function prints the text and writes it back to the text document
    if not re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB',inputText):
        print(inputText)
        open('inputText.txt','w').write(inputText)
# otherwise, the function replaces one word at a time and then calls itself on the output
    for word in re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB',inputText):
        print("Enter a " + word.lower() + ':')
        replacement(re.sub(word,input(),inputText,1))
# break is included here to stop the function once it has written its designated letter
        break
# function is called on the original_input_text to start the program
replacement(original_input_text)
