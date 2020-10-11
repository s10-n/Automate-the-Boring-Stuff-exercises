#! python3
# blankRowInserter.py - takes two integers (N and M) and a spreadsheet filename string as command line arguments, and starting at row N, the program inserts M blank rows into the spreadsheet

import openpyxl,os,sys
from pathlib import Path

#N = int(sys.argv[1])
#M = int(sys.argv[2])
#filename_string = sys.argv[3]
N = 3
M = 2
filename_string = '/home/sean/projects/automate-the-boring-stuff-exercises/Chapter 13/9x9_Multiplication_Table.xlsx'

# read the contents of the spreadsheet
spreadsheet = openpyxl.load_workbook(filename_string)
sheet = spreadsheet.active
max_row = sheet.max_row
max_column = sheet.max_column

# use a for loop to copy the first N lines
# add M to the row number for the remaining lines in the output spreadsheet
#spreadsheet.save(Path(filename_string).stem + '_copy.xlsx')
