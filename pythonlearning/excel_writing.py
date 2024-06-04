import openpyxl

file = '../demo_wr.xlsx'

workbook = openpyxl.load_workbook(file)

# sheet = workbook['Sheet1']
sheet = workbook.active

rows = 5
cols = 4

for r in range (1, rows+1):
    for c in range (1,rows+1):
        sheet.cell(r,c).value='Welcome'

workbook.save(file)