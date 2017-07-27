import pandas as pd
import re

from numpy import NaN

billboard = pd.read_csv('tips.csv')

#Dropping Duplicates
"""
tracks = billboard[['year', 'artist', 'track', 'time']]
print(tracks.info())

tracks_no_duplicates = tracks.drop_duplicates()
print(tracks_no_duplicates.info())
"""

#filling in missing data
# mean average of values = missing values

airquality = pd.read_csv('airquality.csv')

oz_mean = airquality.Ozone.mean()
airquality['Ozone'] = airquality.Ozone.fillna(oz_mean)

print(airquality.info())

#assert

# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()