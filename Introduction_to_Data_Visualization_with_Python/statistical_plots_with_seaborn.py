import pandas as pd
import numpy as np


csv_file = np.genfromtxt('percent-bachelors-degrees-women-usa.csv', delimiter=',')
df = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

year = csv_file[:,0]
physical_sciences = csv_file[:,14]
computer_science = csv_file[:,7]
health = csv_file[:,12]
education = csv_file[:,8]


print(df.columns.get_loc('Education'))

auto_csv = np.genfromtxt('auto-mpg.csv', delimiter=',')
df1 = pd.read_csv('auto-mpg.csv')
print(df1.columns.get_loc('hp'))

mpg = auto_csv[:,0]
hp = auto_csv[:,3]


auto = df1

"""
tips = sns.load_dataset(pd.read_csv('tips.csv'))
sns.lmplot(x= 'total_bill', y='tip', data=tips, hue='sex', palette='Set1')
plt.show()

sns.residplot(x='age', y='fare', data=tips, color='indianred')
plt.show()
"""

import matplotlib.pyplot as plt
import seaborn as sns

sns.lmplot(x='weight', y='hp', data=auto)
plt.show()