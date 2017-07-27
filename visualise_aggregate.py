import pandas as pd
import re
import pandas as pd
import numpy as np
from numpy import NaN

import matplotlib.pyplot as plt

# check data types dtype
gapminder = pd.read_csv('gapminder.csv')

plt.subplot(2, 1, 1)

gapminder.life_expectancy.plot(kind='hist')

gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

print(gapminder_agg.head())
print(gapminder_agg.tail())

plt.subplot(2, 1, 2)

gapminder_agg.plot()

plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

plt.tight_layout()
plt.show()

gapminder.to_csv('gapminder.csv')
gapminder_agg.to_csv('gapminder_agg.csv')

