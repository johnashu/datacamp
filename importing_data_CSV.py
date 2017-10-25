from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
urlretrieve(url, 'winequality-red.csv')

df = pd.read_csv('winequality-red.csv', sep=';')

print(df.iloc[1:2])