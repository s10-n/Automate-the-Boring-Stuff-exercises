import re

urlRegex = re.compile(r'http[s]?://[a-zA-Z0-9.-]+')
#urlRegex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@                 # @ symbol
[a-zA-Z0-9.-]+    # domain name
(\.[a-zA-Z]{2,4}) # country domain
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches =  []
print(urlRegex.findall(text))
