import pandas as pd
def getSheet(file_path, pagename):
    df = pd.read_excel(file_path, sheet_name=pagename)
    return df

def readData(file_path, pagename, row_number, column_number):
    xl = getSheet(file_path, pagename)
    value = xl.iloc[row_number, column_number]
    return value

def writeData(file_path, pagename, data, row_number, column_name):
    xl = getSheet(file_path, pagename)
    xl.loc[row_number, column_name] = data
    writer = pd.ExcelWriter(file_path)
    xl.to_excel(writer, sheet_name=pagename)
    writer.save()
