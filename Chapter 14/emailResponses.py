#! python3
# emailResponses.py - downloads responses from a Google Forms results spreadsheet and outputs a list of email addresses

import ezsheets, re

def email_responses(sheet_ID):
    spreadsheet = ezsheets.Spreadsheet(sheet_ID)
    sheet = spreadsheet[0]
    email_column = sheet.getColumn(2)

    # filter out all non-email results
    return list(filter(lambda entry: re.search('@[a-z]+[\.[a-z]+',entry), email_column))      



