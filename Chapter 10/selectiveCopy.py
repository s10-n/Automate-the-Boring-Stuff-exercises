#! python3
# selectiveCopy.py - walks through a folder tree and searches for files with a certain file extension, then copies these files from whatever location they are in to a new folder
import os, shutil
from pathlib import Path
def selective_copy(source_folder, target_folder, extension):
    # creates the target directory if it doesn't exist already
    try:
        os.mkdir(target_folder)
    except:
        None
    for folderName, subfolders, filenames in os.walk(source_folder):     
        for filename in filenames:
            # copies the file over to the target directory
            if Path(filename).suffix == '.' + extension:
                print(f'Now copying {filename} from {folderName} to {target_folder}')
                shutil.copy(Path(folderName) / filename, target_folder)

selective_copy(Path('C:\\Users\\User\\Documents'),Path('C:\\Users\\User\\Desktop\\PDFs'),'pdf')
