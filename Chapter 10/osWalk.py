import os
for folderName, subfolders, filenames in os.walk('c:/Users/User/mu_code/Automate the Boring Stuff'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')
