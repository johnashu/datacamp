import pandas as pd

jan = pd.read_csv('sales-jan-2015.csv', index_col='Date', parse_dates=True)

feb = pd.read_csv('sales-feb-2015.csv', index_col='Date', parse_dates=True)

mar = pd.read_csv('sales-mar-2015.csv', index_col='Date', parse_dates=True)

jan_units = jan['Units']

feb_units = feb['Units']
mar_units = mar['Units']

quarter1 = jan_units.append(feb_units).append(mar_units)


print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])
print(quarter1.sum())


units = []

for month in [jan, feb, mar]:
    units.append(month['Units'])


quarter1 = pd.concat(units, axis='rows')

print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])

