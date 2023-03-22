import pandas as pd
file_name='TS_sales_dataset_ver02.xlsx'
df=pd.read_excel(file_name)


df.info() 

print('df',df.shape)
