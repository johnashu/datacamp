import pandas as pd

uber1 = pd.read_csv('uber1.csv')
uber2 = pd.read_csv('uber2.csv')
uber3 = pd.read_csv('uber3.csv')

row_concat = pd.concat([uber1, uber2, uber3])
#print(row_concat.shape)
#print(row_concat.head())


# combining columns of data
ebola = pd.read_csv('ebola.csv')
status_country = pd.read_csv('ebola.csv')
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

#print(ebola_tidy.shape)
#print(ebola_tidy.head())


# LGON LONG GLOB GLOB

import glob
import pandas as pd

pattern = '*.csv'
csv_files = glob.glob(pattern)
#print(csv_files)
csv2 = pd.read_csv(csv_files[1])
#print(csv2.head())


#iterating and concatenating
frames = []

for csv in csv_files:
    df = pd.read_csv(csv)
    frames.append(df)

uber = pd.concat(frames)   
print(uber.shape) 
print(uber.head())


#Merging Data Like SQL 
# combine disparate datasets based on common columns

# 1-1 merge
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')
print(o2o)

#many-to-1 data merge

m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')
print(m2o)
