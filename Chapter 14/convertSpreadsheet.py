x#! python3
# convertSpreadsheet.py - uses Google Sheets to convert a spreadsheet file into other formats

import ezsheets
from pathlib import Path

def convert_spreadsheet(target_path):

    # upload the spreadsheet
    spreadsheet = ezsheets.upload(target_path)

    # get the uploaded spreadsheet's file name
    filename = Path(target_path).stem
    destination_file_type = input('Select the destination filetype (Excel / ODS / CSV / TSV / PDF / HTML): ')

    # download the selected filetype from Google Sheets and prints a download message
    def change_download_format(extension):
        spreadsheet.downloadAsExcel(filename + extension)
        print(Path(target_path).name + f' converted to {filename}{extension}')

    # determines which filetype to download
    if destination_file_type.lower() == 'excel':
        change_download_format('.xlsx')
    elif destination_file_type.lower() == 'ods':
        change_download_format('.ods')
    elif destination_file_type.lower() == 'csv':
        change_download_format('.csv')
    elif destination_file_type.lower() == 'tsv':
        change_download_format('.tsv')
    elif destination_file_type.lower() == 'pdf':
        change_download_format('.pdf')
    elif destination_file_type.lower() == 'html':
        change_download_format('.zip')

    # delete the uploaded spreadsheet
    spreadsheet.delete()

convert_spreadsheet('/home/sean/projects/automate-the-boring-stuff-exercises/Chapter 13/9x9_Multiplication_Table.xlsx')
