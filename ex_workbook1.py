import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.Workbook() #새로운 Workbook 객체 생성
 #객체를 출력해보기

path = r"C:\Users\KW\Documents\Python_Project"

wb = op.load_workbook(path + "/test.xlsx")

print(wb)