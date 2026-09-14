"""
We want to perform some calculations on a worksheet
"""

import datetime as dt
from pathlib import Path

import openpyxl

PATH = Path(__file__).resolve().parents[0]
print(PATH)
FILE = PATH / 'example.xlsx'

workbook = openpyxl.load_workbook(FILE)
sheet = workbook.active

# ===============================================
# Calculating Age with date of birth and datetime
# ===============================================

# The range is chosen according to the worksheet's layout. 
# The values appear at rows 5 to 9
# for row in range(5, 10):    
#     today = dt.datetime.now()
#     date = sheet[f'C{row}'].value

#     # Convert strings to datetime objects
#     if isinstance(date, str):
#         date = dt.datetime.strptime(date, "%m/%d/%Y")

#     age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
#     sheet[f'D{row}'] = age

# workbook.save(FILE)
# ===============================================
# Changing the currency
# ===============================================
# We need to install the pandas-datareader module for this:
#       pip install pandas-datareader
# Other options include: webscraping, apis and forex module for python

import pandas_datareader as web

for row in range(5, 10):
    today = dt.datetime.now()
    date = sheet[f'C{row}'].value

    # Convert strings to datetime objects
    if isinstance(date, str):
        date = dt.datetime.strptime(date, "%m/%d/%Y")

    age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
    sheet[f'D{row}'] = age

    usd_to_euro = web.get_data_fred('DEXUSEU') .iloc[-1]['DEXUSEU']     
    # We want to convert from USD to Euros by division
    sheet[f'E{row}'] = sheet[f'E{row}'].value / usd_to_euro
    # Change number format
    sheet[f'E{row}'].number_format = "#,##0.00€"

workbook.save(FILE)