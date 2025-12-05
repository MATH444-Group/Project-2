import os
import pandas as pd





def importData(data_path: os.path):

  if not os.path.exists(data_path):
    print('Data not found at', data_path)
    print('Current working directory:\n\t', os.getcwd())
    exit(1)

  df = pd.read_csv(data_path)
  
  return df