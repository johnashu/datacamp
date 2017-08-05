import pandas as pd

from glob import glob

filenames = glob('*.csv')

dataframes = [pd.read_csv(f) for f in filenames]

print(dataframes[0].head())

bronze = pd.read_csv('Bronze.csv')
silver = pd.read_csv('Silver.csv')
gold = pd.read_csv('Gold.csv')

print(gold.head())

medals = gold.copy()
new_labels = ['NOC', 'Country', 'Gold']
medals.columns = new_labels
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']


print(medals.head())
