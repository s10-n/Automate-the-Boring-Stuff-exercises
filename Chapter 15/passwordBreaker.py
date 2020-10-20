#! python3
# passwordBreaker.py - decrypts a PDF by trying every possible English word until it finds one that works

import PyPDF2,re

# gets the pdf's path from the command line
pdf_path = sys.argv[1]

# pulls a list of words from the supplied dictionary file and removes the newline from each one
dictionary_list = [re.sub('\n','',item) for item in open('dictionary.txt','r').readlines() if True]

# open the pdf
pdf_reader = PyPDF2.PdfFileReader(open(pdf_path,'rb'))

# function that decrypts the pdf
def decrypt_with(word):
    print(f'Attempting to decrypt with password {word}...')

    # test if the decryption was successful
    decryption_successful = pdf_reader.decrypt(word)
    if not decryption_successful:
        print('Decryption unsuccessful')
    else:
        print(f'Decryption successful. Password = {word}.')
    return decryption_successful

# try testing each word in the dictionary along with its lowercase and Titlecase counterpart, breaking when it successfully decrypts the file
for word in dictionary_list:
    if decrypt_with(word) or decrypt_with(word.lower()) or decrypt_with(word.title()):
        break
