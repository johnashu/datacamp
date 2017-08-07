import pandas as pd
"""
software = pd.read_csv('feb-sales-Software.csv', parse_dates=['Date']).sort_values('Date')
hardware = pd.read_csv('feb-sales-Hardware.csv', parse_dates=['Date']).sort_values('Date')

pd.merge(hardware, software, how='outer')

print(pd.merge_ordered(hardware, software, on=['Date', 'Company'], suffixes=('_hardware', '_software')).head())


tx_weather = pd.merge_ordered(austin, houston)

print(tx_weather)

tx_weather_suff = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'])

print(tx_weather_suff)

tx_weather_ffill = pd.merge_ordered(austin, houston, on='date', suffixes=['_aus', '_hus'], fill_method='ffill')

print(tx_weather_ffill)

"""

oil = pd.read_csv('oil_price.csv', parse_dates=['Date']).sort_values('Date')
auto = pd.read_csv('auto-mpg.csv').sort_values('yr')

print(oil)
print(auto)

# Merge auto and oil: merged
merged = pd.merge_asof(auto, oil, left_on='yr', right_on='Date')

# Print the tail of merged
print(merged.tail())

# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)

# Print yearly.corr()
print(yearly.corr())