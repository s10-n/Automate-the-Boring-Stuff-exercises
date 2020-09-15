#! python3
# mapIt.py - gets a street address from the command line arguments or clipboard and opens the web browswer to the Google Maps page for the address

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # read the command line arguments from sys.argv
    address = ' '.join(sys.argv[1:])
else:
    # read the clipboard contents
    address = pyperclip.paste()
# call the webbrowser.open() function to open the web browser
webbrowser.open('https://www.google.com/maps/place/' + address)
