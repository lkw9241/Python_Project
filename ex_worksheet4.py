import  openpyxl  as  op
wb = op.load_workbook(r"C:\Users\KW\Documents\Python_Project\test.xlsx")
ws_list = wb.sheetnames 

for sht in ws_list:
    ws=wb[sht]

print(ws)