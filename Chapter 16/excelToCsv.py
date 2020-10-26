#! python3
# excelToCsv.py - reads all of the Excel files in the current working directory and outputs them as CSV files

import csv,openpyxl
from pathlib import Path

for excelFile in os.listdir('.'):
    
    # skip non-xlsx files
    if not excelFile.endswith('.xlsx'):
        continue
    print(f'Converting {excelFile} to .csv...')
    
    # load the workbook object
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.get_sheet_names():
        
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)
        
        # create the CSV filename from the Excel filename and sheet title.
        csvFilename = Path(excelFile).stem + '_' + sheet.title + '.csv'
        csvFile = open(csvFilename,'w',newline='')
        
        # Create the csv.writer object for this CSV file.
        csvWriter = csv.writer(csvFile)
        
        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = [] # append each cell to this list
            
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):

                # Append each cell's data to rowData
                rowData.append(sheet.cell(row=rowNum, column=colNum).value)
                
            # Write the rowData list to the CSV file.                
            csvWriter.writerow(rowData)
        print(f'Wrote {csvFilename}')
        csvFile.close()
