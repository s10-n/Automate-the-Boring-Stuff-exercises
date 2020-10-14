#! python3
# findingMistakes.py - checks Al Sweigart's Bean Count spreadsheet, finding the mistake and printing the correct numbers

import ezsheets

# get the spreadsheet and the first sheet
bean_spreadsheet = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
bean_sheet = bean_spreadsheet[0]

# filter out any whitespace rows to determine the number of actual entries
number_of_entries = len(list(filter(lambda entry: len(entry) > 1, bean_sheet.getColumn(1))))

# for each actual row, check if the multiplication is correct
for row_number in range(2,number_of_entries):
    row = bean_sheet.getRow(row_number)
    if (int(row[0]) * int(row[1])) != int(row[2]):

        # print the row number, incorrect value, and correct value
        print(f'Error in row {row_number}.\nValues shown: {row[0]} * {row[1]} = {row[2]}.\nCorrect values: {row[0]} * {row[1]} = {int(row[0]) * int(row[1])}.')
