import pandas as pd
import re
import pandas as pd
import numpy as np
from numpy import NaN


g1800s = pd.read_csv('gapminder.csv')
g1900s = pd.read_csv('gapminder.csv')
g2000s = pd.read_csv('gapminder.csv')

import matplotlib.pyplot as plt

g1800s.plot(kind='scatter', x='1800', y='1899')

plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

plt.xlim(20, 55)
plt.ylim(20, 55)
plt.show()


def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

#assert g1800s.columns[0] == 'Life expectancy'
#assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()
#assert g1800s['Life expectancy'].value_counts()[0] == 1


#concatenate

gapminder = pd.concat([g1800s, g1900s, g2000s])
print(gapminder.shape)
print(gapminder.head())

# reshape

gapminder_melt = pd.melt(gapminder, id_vars='Life expectancy')
gapminder_melt.columns = ['country', 'year', 'life_expectancy']
print(gapminder_melt.head())

# check data types dtype
gapminder = pd.read_csv('gapminder.csv')

gapminder.year = pd.to_numeric(gapminder.year)
assert gapminder.country.dtypes == np.object
assert gapminder.year.dtypes == np.int64
assert gapminder.life_expectancy.dtypes == np.float64

#country spellings
countries = gapminder['country']
countries= countries.drop_duplicates()
pattern = '^[A-Za-z\.\s]*$'
mask = countries.str.contains(pattern)
mask_inverse = ~mask
invalid_countries = countries.loc[mask_inverse]
print(invalid_countries)