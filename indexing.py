
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = 'pennsylvania2012_turnout.csv'


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
print(high_turnout_df)#

import numpy as np

too_close = election['margin'] < 1
election.loc[too_close, 'winner'] = np.nan
print(election.info())

titanic = pd.read_csv('titanic.csv')

df = titanic[['age', 'cabin']]
print(df.shape)

print(df.dropna(how='any').shape)

print(df.dropna(how='all').shape)
print(titanic.dropna(thresh=1000, axis='columns').info())

# FLoor Divsion

#df.floordiv(12)

#np.floor_divide(df, 12)

#def dozens(n):
#    return n // 12

#print(df.apply(dozens))

#df.apply(lambda n: n // 12)

#df['dozens_of_eggs'] = df.name.floordiv(12)

#df.index = df.index.str.upper()
#print(df)

#df.index = df.index.map(str.lower)
#df['salty_eggs'] = df.salt + df.dozens_of_eggs

weather = pd.read_csv('pittsburgh2013.csv')


def to_celsius(F):
    return 5/9*(F - 32)

df_celsius = weather[['Mean TemperatureF','Mean Dew PointF']].apply(to_celsius)

df_celsius.columns = ['Mean TemperatureC','Mean Dew PointC'] 

print(df_celsius.head())

red_vs_blue = {'Obama':'blue', 'Romney': 'red'}
election['color'] = election['winner'].map(red_vs_blue)
print(election.head())

from scipy.stats import zscore

turnout_zscore = zscore(election['turnout'])
print(type(turnout_zscore))

election['turnout_zscore'] = turnout_zscore

print(election.head())


# changing the index of a dataframe

sales = pd.read_csv('sales.csv')
print(sales)
"""
### numpy.int64' object has no attribute 'upper' ###

new_idx = [month.upper() for month in sales.index]
sales.index = new_idx
print(sales)

"""

sales.index.name = 'MONTHS'
sales.columns.name = 'PRODUCTS'
print(sales)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

sales.index = months
print(sales)


# pivot 

users =pd.read_csv('users.csv')

visitors_pivot = users.pivot(index='weekday', columns='city', values='visitors')
#print(visitors_pivot)

signups_pivot = users.pivot(index='weekday', columns='city', values='signups')
#print(signups_pivot)

pivot = users.pivot(index='weekday', columns='city')
print(pivot)


"""
byweekday = users.unstack('weekday')
print(byweekday)
print(byweekday.stack(level='weekday'))


bycity = users.unstack('city')
print(bycity)
print(bycity.stack(level="city"))

newusers =  bycity.stack(level='city')
newusers = newusers.swaplevel(0, 1)
print(newusers)
newusers = newusers.sort_index()
print(newusers)
print(newusers.equals(users))

AttributeError: 'Series' object has no attribute 'stack'

"""

skinny = pd.melt(users, id_vars=['weekday', 'city'])

print(skinny)

users_idx = users.set_index(['city', 'weekday'])
print(users_idx)
kv_pairs = pd.melt(users_idx, col_level=0)
print(kv_pairs)

