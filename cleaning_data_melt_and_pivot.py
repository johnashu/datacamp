import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#melt

airquality = pd.read_csv('airquality.csv')

print(airquality.head())

airquality_melt = pd.melt(airquality, id_vars = ['Month', 'Day'], var_name='measurement', value_name='reading' )

print(airquality_melt.head())


#pivot

airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')
print(airquality_pivot.head())


#RESET the index of a dataframe
print(airquality_pivot.index)

airquality_pivot = airquality_pivot.reset_index()

print(airquality_pivot.index)
print(airquality_pivot.head())


# Pivot Duplicate values

airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

airquality_pivot = airquality_pivot.reset_index()

print(airquality_pivot.head())
print(airquality.head())