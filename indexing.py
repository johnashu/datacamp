
import numpy as np
import matplotlib.pyplot as plt

filename = 'pennsylvania2012_turnout.csv'

import pandas as pd

election = pd.read_csv(filename, index_col='county')

results = election[['winner', 'total', 'voters']]

print(results.head())

x = 4
y = 4

print(election.iloc[x, y] == election.loc['Bedford', 'winner'])



p_counties = election['Perry':'Potter']
print(p_counties)

p_counties_rev = election['Potter':'Perry':-1]
print(p_counties_rev)

left_columns = election.loc[:, :'Obama']
print(left_columns.head())

middle_columns = election.loc[:, 'Obama':'winner']
print(middle_columns.head())

right_columns = election.loc[:, 'Romney':]
print(right_columns.head()) 

rows = ['Philadelphia', 'Centre', 'Fulton']

cols = ['winner', 'Obama', 'Romney']
three_counties = election.loc[rows, cols]
print(three_counties)

high_turnout = election['turnout'] > 70
high_turnout_df = election.loc[high_turnout]
print(high_turnout_df)

