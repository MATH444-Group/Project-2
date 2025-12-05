from datetime import datetime
import pandas as pd



"""
Data Pre-Processing to Extract Additional Useful Information

[SUMMARY]
- Replace 'Year' with a more useful metric, 'Age'\
- Drop attribute 'Model'
- Replace 'Engin', 'Max Power', and 'Max Torque' with int value equivalents
"""
def processData(df):
  
  df['Age'] = datetime.now().year - df['Year']
  df.drop('Year', axis = 1, inplace = True)



  df.drop(labels='Model',axis= 1, inplace = True)



  df['Engine'] = df['Engine'].str.extract(r'(\d+\.?\d*)', expand=False).astype(float).astype(int)
  df['Max Power'] = df['Max Power'].str.extract(r'(\d+\.?\d*)', expand=False).astype(float).astype(int)
  df['Max Torque'] = df['Max Torque'].str.extract(r'(\d+\.?\d*)', expand=False).astype(float).astype(int)



  return df