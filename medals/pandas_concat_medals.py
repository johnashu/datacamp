import pandas as pd

from glob import glob

bronze = pd.read_csv('bronze_top5.csv', index_col=0)
silver = pd.read_csv('silver_top5.csv', index_col=0)
gold = pd.read_csv('gold_top5.csv', index_col=0)


medal_types = ['bronze', 'silver', 'gold']

medals = []

for medal in medal_types:
    file_name = '%s_top5.csv' % medal
    columns = ['Country', medal]
    medal_df = pd.read_csv(file_name, header=0, index_col='Country', names=columns)
    medals.append(medal_df)

medals = pd.concat(medals, axis='columns', keys=medal_types)

print(medals)

medal_list = [bronze, silver, gold]

medals = pd.concat(medal_list, keys=['bronze', 'silver','gold'], axis=1, join='inner')

print(medals)


"""

***KeyError: 'the label [bronze] is not in the [index]'***

medals_sorted = medals.sort_index(level=0)
print(medals_sorted.loc[('bronze','Germany')])
print(medals_sorted.loc['silver'])

idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:, 'United Kingdom'], :])


****NO CHINA VARIABLE..***

china_annual = china.resample('A').pct_change(10).dropna()

us_annual = us.resample('A').pct_change(10).dropna()

gdp = pd.concat([china_annual, us_annual], axis=1, join='inner')

print(gdp.resample('10A').last())

"""

