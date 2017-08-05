import pandas as pd

def sales():
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

#sales()

names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'])
names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'])

names_1881['year'] = 1881
names_1981['year'] = 1981


combined_names = names_1881.append(names_1981, ignore_index=True)

print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)

print(combined_names.loc[combined_names['name'] == 'John'])

