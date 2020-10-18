#! python3
# pdfDecrypter.py - finds all encrypted PDFs in a folder (and its subfolders) and creates a decrypted copy of the PDF using a provided password

import os,PyPDF2,sys,re
from pathlib import Path

# ensure that the command is being used correctly
if len(sys.argv) != 2:
    print('pdfDecrypter is used with a single command line argument, which is used to decrypt any encrypted files.')
else:
    password = sys.argv[1]

    # walk through the current directory
    for folder_name, subfolders, filenames in os.walk(os.getcwd()):
        for filename in filenames:

            # if the file is an encrypted pdf, open it
            if Path(filename).suffix == '.pdf':
                pdf_reader = PyPDF2.PdfFileReader(open(filename,'rb'))
                if pdf_reader.isEncrypted:
                    can_be_decrypted = False
                    print(f'Opening {filename}')

                    # check if the file can be decrypted with the given password
                    try:
                        pdf_reader.decrypt(password)
                        pdf_reader.getPage(0)
                        can_be_decrypted = True
                        
                    # if the supplied password doesn't work, let the user know and move on
                    except:
                        print(f'Incorrect password for {filename}.')

                    # if the password does work, create an decrypted copy of the file
                    if can_be_decrypted:
                        print(f'Now decrypting {filename}...')
                        pdf_writer = PyPDF2.PdfFileWriter()
                        for page_num in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(page_num))

                        # rename the file and remove '_encrypted' from the name if present
                        if re.search('_encrypted',filename):
                            decrypted_filename = re.sub('_encrypted','_decrypted',filename)
                        else:
                            decrypted_filename = str(Path(filename).stem) + '_decrypted.pdf'
                        decrypted_pdf = open(decrypted_filename,'wb')
                        pdf_writer.write(decrypted_pdf)
                        print(f'File decrypted as {decrypted_filename}.')
                        decrypted_pdf.close()
