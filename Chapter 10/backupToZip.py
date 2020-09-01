#! python3
# backupToZip.py - copies an entire folder and its contents into a ZIP file whose filename increments
import zipfile,os
def backupToZip(folder):
    # back up the entire contents of 'folder' into a zip file
    folder = os.path.abspath(folder) # make sure folder is absolute
    # figure out the filename this code should use based on what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    # todo: create the zip file
    # todo walk the entire folder tree and compress the files in each folder
    print('Done.')
#backupToZip('c:/Users/User/mu_code/Automate the Boring Stuff/Chapter 10')
