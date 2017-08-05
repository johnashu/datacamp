import pandas as pd

filenames = ['tips.csv', 'sales.csv']

dataframes = [pd.read_csv(f) for f in filenames]

for f in filenames:
    dataframes.append(pd.read_csv(f))

print(dataframes)

