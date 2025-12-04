import os
import pandas as pd



___DATA_DIR___ = '../data/cleaned/'
___DATA_FILE__ = 'cleaned car details v4.csv'
___DATA_PATH___ = os.path.join(___DATA_DIR___, ___DATA_FILE__)



def exportData(df):
  df.to_csv(___DATA_PATH___, index=False)