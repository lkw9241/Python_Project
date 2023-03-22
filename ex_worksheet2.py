import  openpyxl  as  op  #openpyxl 모듈 import
wb = op.load_workbook(r"C:\Users\KW\Documents\Python_Project\test_result.xlsx")
ws_list = wb.sheetnames  #해당 Workbook의 시트 목록을 리스트로 저장
print(ws_list) #리스트 출력