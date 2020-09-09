# creatingAGap.py - inserts a gap into numbered files after file n, with n as one of the variables passed to the function
import os,re
from pathlib import Path

def gap_creator(prefix,target_folder,gap_target): # string, path, int
    filename_regex = re.compile(r'\d+\b')
    # filters list by two lambdas, one which determines it has the correct prefix in it and one which determines it has a number in the last position of the filename
    filtered_list = list(filter(lambda file: re.search(filename_regex,file),list(filter(lambda file: prefix in file,os.listdir(target_folder)))))
    # iterates through the filtered list, which is enumerated to determine the correct number of the file
    print(f"Numbered files with prefix '{prefix}':")
    # creates an empty dictionary of name changes
    name_changes = {}
    for idx,file in enumerate(filtered_list,start=1):
        # collects the number from the filename
        file_number = re.search(filename_regex,Path(file).stem).group()
        # if the file's number doesn't match up with its place in the folder, adds the file's name to a list of files to be renamed
        if idx > gap_target:
            name_changes[file] = (prefix + ('0' * (len(file_number)-len(str(idx))) + str(idx+1) + str(Path(file).suffix)))
            # appends 'temp' to file name so that file can be overwritten with no issues
            os.rename(target_folder + file, target_folder + file + "temp")
        else:
            print(file)
    for filename in name_changes:
        # renames files to the name assigned to them in the dictionary
        os.rename(target_folder + filename + 'temp', target_folder + name_changes[filename])
        print(f'{filename} renamed to {name_changes[filename]}')

gap_creator('spam','c:/Users/User/mu_code/Automate the Boring Stuff/Chapter 10/gap_filler files/',2)
