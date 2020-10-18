#! python3
# pdfParanoia.py - goes through every PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on the command line, then saves each encrypted PDF with an _encrypted.pdf suffix added to the original filename

import os,PyPDF2,sys
from pathlib import Path

# ensure that the command is being used correctly
if len(sys.argv) != 2:
    print('pdfParanoia is used with a single command line argument, which becomes the password for the encrypted files.')
else:
    password = sys.argv[1]

    # walk through the current directory
    for folder_name, subfolders, filenames in os.walk(os.getcwd()):
        for filename in filenames:

            #if a file is a pdf, open it
            if Path(filename).suffix == '.pdf':
                pdf_reader = PyPDF2.PdfFileReader(open(filename, 'rb'))

                # if the file is not already encrypted, write all of the pages to a new file to encrypt
                if not pdf_reader.isEncrypted:
                    print(f'Now encrypting {filename}...')
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))
                    pdf_writer.encrypt(password)
                    encrypted_filename = f'{Path(filename).stem}_encrypted.pdf'
                    encrypted_pdf = open(encrypted_filename,'wb')
                    pdf_writer.write(encrypted_pdf)
                    print(f'File encrypted as {encrypted_filename}.')
                    encrypted_pdf.close()

                    # test if the newly created file is encrypted properly
                    try:
                        pdf_reader = PyPDF2.PdfFileReader(open(encrypted_filename,'rb'))
                        pdf_reader.decrypt('password')
                    except:
                        print('File not encrypted correctly.')

                    # delete the unencrypted original file
                    os.remove(filename)
                    print(f'{filename} deleted.')
