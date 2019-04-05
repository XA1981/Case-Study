import pandas as pd 
import xlrd
import numpy as np

df = pd.read_excel("PythonTest.xlsx") 

print('after reading file --> '+df)

df['Name'] = np.where(df['Emp_Id']>105, 'Abhi', df['Name'])
print('after updation --> '+df)
