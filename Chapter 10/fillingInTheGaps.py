# fillingInTheGaps.py - finds all files with a given prefix in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt), and renames all the later files to close this gap

import os,re
from pathlib import Path

def gap_filler(prefix,target_folder): # string, path
    filename_regex = re.compile(r'\d+\b')
    # filters list by two lambdas, one which determines it has the correct prefix in it and one which determines it has a number in the last position of the filename
    filtered_list = list(filter(lambda file: re.search(filename_regex,file),list(filter(lambda file: prefix in file,os.listdir(target_folder)))))
    # iterates through the filtered list, which is enumerated to determine the correct number of the file
    print(f"Numbered files with prefix '{prefix}':")
    for idx,file in enumerate(filtered_list,start=1):
        # collects the number from the filename
        file_number = re.search(filename_regex,Path(file).stem).group()
        # if the file's number doesn't match up with its place in the folder, it is renamed
        if idx != int(file_number):
            new_name = (prefix + ('0' * (len(file_number)-len(str(idx))) + str(idx) + str(Path(file).suffix)))
            os.rename(target_folder + file, target_folder + new_name)
            print(f'{file} renamed to {new_name}')
        else:
            print(file)

gap_filler('spam','c:/Users/User/mu_code/Automate the Boring Stuff/Chapter 10/gap_filler files/')
