import os
import pandas as pd







def exportData(df, data_path):
  df.to_csv(data_path, index=False)