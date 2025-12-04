import os
import pandas as pd



___DATA_DIR___ = '../data/raw/'
___DATA_FILE__ = 'car details v4.csv'
___DATA_PATH___ = os.path.join(___DATA_DIR___, ___DATA_FILE__)



def importData():

  if not os.path.exists(___DATA_PATH___):
    print('Data not found at', ___DATA_PATH___)
    print('Current working directory:\n\t', os.getcwd())
    exit(1)

  df = pd.read_csv(___DATA_PATH___)
  
  return df