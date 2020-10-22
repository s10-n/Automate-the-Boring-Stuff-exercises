#! python3
# removeCsvHeader.py - removes the header from all CSV files in the current working directory

import csv, os
os.makedirs('headerRemoved',exist_ok=True)

# loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + ' ...')

    # read the CSV file in (skipping the first row).
    csvRows = []
    csvFileObject = open(csvFilename)
    readerObject = csv.reader(csvFileObject)
    for row in readerObject:
        if readerObject.line_num == 1:
            continue # skip the first row
        csvRows.append(row)
    csvFileObject.close()
    
    # write out the CSV file
    csvFileObject = open(os.path.join('headerRemoved', csvFilename), 'w', newline = '')
    csvWriter = csv.writer(csvFileObject)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObject.close()
