from utils.cleanData import cleanData
from utils.exportData import exportData
from utils.importData import importData
from utils.processData import processData



def main():

  df = importData()
  df = cleanData(df)
  df = processData(df)
  exportData(df)





if __name__ == "__main__":
  main()