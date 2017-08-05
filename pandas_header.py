import pandas as pd

from glob import glob

filenames = glob('*.csv')

dataframes = [pd.read_csv(f) for f in filenames]

print(dataframes[0].head())


