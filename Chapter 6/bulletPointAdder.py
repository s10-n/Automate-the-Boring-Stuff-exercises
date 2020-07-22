#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each of line of text on the clipboard
import pyperclip
text = pyperclip.paste()
# separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
# TODO: separate lines and add stars
pyperclip.copy(text)