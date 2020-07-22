# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()
VOWELS = ('a','e','i','o','u')
pigLatin = [] # a list of the words in Pig Latin
for word in message.split():
    # separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    # separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    # remember if the word was in uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()
    # separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    # add the pig latin ending to the word:
    if prefixConsonants !='':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    # set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    # add the non-letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
print(' '.join(pigLatin))
