from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt

url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
#urlretrieve(url, 'winequality-red.csv')

xl = pd.read_excel(url, sheetname=None)
print(xl.keys())
print(xl['1700'].head())

