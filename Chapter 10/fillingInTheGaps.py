# fillingInTheGaps.py - finds all files with a given prefix in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt), and renames all the later files to close this gap

import os,re
from pathlib import Path

def gap_filler(prefix,target_folder): # string, path
    filename_regex = re.compile(r'\d+\b')
    # filters list by two lambdas, one which determines it has the correct prefix in it and one which determines it has a number in the last position of the filename
    filtered_list = list(filter(lambda file: re.search(filename_regex,file),list(filter(lambda file: prefix in file,os.listdir(target_folder)))))
    for file_number,file in enumerate(filtered_list,start=1):
        if file_number == int(re.search(filename_regex,Path(file).stem).group()):
            print(int(re.search(filename_regex,Path(file).stem).group()))
        #print(file_number)
 #       print(int(re.search(filename_regex,Path(file).stem).group()))
    
# list all of the files in a folder with a given prefix
# iterate through those files in order to ensure that there is a number
# if there is a gap, rename the files to close this gap

gap_filler('spam','c:/Users/User/mu_code/Automate the Boring Stuff/Chapter 10/gap_filler files/')
