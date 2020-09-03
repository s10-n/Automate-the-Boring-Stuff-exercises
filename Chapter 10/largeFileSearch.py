#! python3
# largeFileSearch.py - walks through a folder tree and searches for files or folders with a file size of more than 100MB, then prints these files with their absolute path to the screen

import os
from pathlib import Path

def large_file_search(folder_tree,file_size): # file size should be in bytes
    def size_checker(object_to_check):
        if os.path.getsize(Path(folderName) / Path(object_to_check)) > file_size:
            print(Path(folderName) / Path(object_to_check))
    for folderName, subfolders, filenames in os.walk(folder_tree):
        for subfolder in subfolders:
            size_checker(subfolder)
        for filename in filenames:
            size_checker(filename)
