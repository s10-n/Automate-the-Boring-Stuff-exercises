#! python3
# largeFileSearch.py - walks through a folder tree and searches for files or folders with a file size of more than 100MB, then prints these files with their absolute path to the screen

import os
from pathlib import Path

def large_file_search(folder_tree,file_size): # file size should be in bytes
    for folderName, subfolders, filenames in os.walk(folder_tree):
        

p = Path('c:/Users/User/Desktop/Movies/A.Scene.At.The.Sea.1991.DVDRip.XviD/A Scene at the Sea.avi')
print(str(round(os.path.getsize(p)/1000000,2)) + ' MB')

