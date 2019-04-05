import pandas as pd 
import xlrd
import numpy as np

df = pd.read_excel("/home/osboxes/Public/PythonTest.xlsx") 

print(df)

df['Name'] = np.where(df['Emp_Id']>105, 'Abhi', df['Name'])
print(df)
