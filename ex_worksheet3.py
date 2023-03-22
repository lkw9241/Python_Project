import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook(r"C:\Users\KW\Documents\Python_Project\test_result.xlsx")

ws_list = wb.sheetnames  #해당 Workbook의 시트 목록을 리스트로 저장

for  sht  in  ws_list:
    ws = wb[sht] #Sheet 객체 생성, 객체[]-> 리스트양식 a[0]_a객체의 0번째 요소
    print(ws) #객체 출력