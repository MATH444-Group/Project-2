import pandas as pd



"""
Count the number of null values in data frame
- True if numNullValues is not 0
- False if passed data frame has no null values
"""
def hasNull(df):

  numNullValues = df.isna().sum().sum()
  
  if numNullValues != 0:
    return True
  return False



def cleanData(df):

  if hasNull(df):
    df = df.dropna()

  return df