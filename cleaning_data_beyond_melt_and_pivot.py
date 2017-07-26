import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tb = pd.read_csv('tb.csv')

#melt tb
tb_melt = pd.melt(tb, id_vars=['country', 'year'])

#creat a Gender column
tb_melt['gender'] = tb_melt.variable.str[0]

# create age group cOlumn
tb_melt['age_group'] = tb_melt.variable.str[1:]

print(tb_melt.head())

#Spliting a column with split an get

ebola = pd.read_csv('ebola.csv')

ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')
ebola_melt['type'] = ebola_melt.str_split.str.get(0)
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

print(ebola_melt.head())