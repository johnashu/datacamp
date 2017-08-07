
import pandas as pd

file_path_editions = 'Summer Olympic medalists 1896 to 2008 - EDITIONS.tsv'

editions = pd.read_csv(file_path_editions, sep='\t')

editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

print(editions)

file_path_ioc = 'Summer Olympic medalists 1896 to 2008 - IOC COUNTRY CODES.csv'

ioc_codes = pd.read_csv(file_path_ioc)

ioc_codes = ioc_codes[['Country', 'NOC']]
print(ioc_codes.head())
print(ioc_codes.tail())

medals_dict = {}

for year in editions['Edition']:
    file_path = 'summer_{:d}.csv'.format(year)
    medals_dict[year] = pd.read_csv(file_path)
    medals_dict[year] = medals_dict[year][['Athlete', 'NOC', 'Medal']]
    medals_dict[year]['Edition'] = year
    
medals = pd.concat(medals_dict, ignore_index=True)

print(medals.head())


medal_counts = medals.pivot_table(aggfunc='count', index='Edition', values='Athlete', columns='NOC' )
print(medal_counts.head())
print(medal_counts.tail())


totals = editions.set_index('Edition')
totals = totals['Grand Total']
fractions = medal_counts.divide(totals, axis='rows')

print(fractions.head())
print(fractions.tail())

mean_fractions = fractions.expanding().mean()

fractions_change = mean_fractions.pct_change() * 100

fractions_change = fractions_change.reset_index()
print(fractions_change.head())
print(fractions_change.tail())



hosts = pd.merge(editions, ioc_codes, how='left')

hosts = hosts[['Edition','NOC']].set_index('Edition')
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'

hosts = hosts.reset_index()

print(hosts)



reshaped = pd.melt(fractions_change, id_vars='Edition', value_name='Change')
print(reshaped.shape, fractions_change.shape)

chn = reshaped.loc[reshaped.NOC == 'CHN']

print(chn.tail())




merged = pd.merge(reshaped, hosts)

print(merged.head())

influence = merged.set_index('Edition').sort_index()


print(influence.head())


import matplotlib.pyplot as plt

change = influence['Change']

ax = change.plot(kind='bar')

ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])


plt.show()