import pandas as pd
import numpy as np


csv_file = np.genfromtxt(
    'percent-bachelors-degrees-women-usa.csv', delimiter=',')
df = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

year = csv_file[:, 0]
physical_sciences = csv_file[:, 14]
computer_science = csv_file[:, 7]
health = csv_file[:, 12]
education = csv_file[:, 8]


print(df.columns.get_loc('Education'))

auto_csv = np.genfromtxt('auto-mpg.csv', delimiter=',')
df1 = pd.read_csv('auto-mpg.csv')
print(df1.columns.get_loc('hp'))

mpg = auto_csv[:, 0]
hp = auto_csv[:, 3]

auto = df1

tips_csv = pd.read_csv('tips.csv')
tips = tips_csv

import matplotlib.pyplot as plt
import seaborn as sns

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='Set1')
plt.show()

sns.residplot(x='total_bill', y='tip', data=tips, color='indianred')
plt.show()

sns.stripplot(x='day', y='tip', data=tips)
plt.ylabel('tip ($)')
plt.show()

sns.stripplot(x='day', y='tip', data=tips, jitter=True, size=4)
plt.ylabel('tip ($)')
plt.show()

sns.swarmplot(x='day', y='tip', data=tips)
plt.ylabel('tip ($)')
plt.show()

sns.swarmplot(x='day', y='tip', data=tips, hue='sex')
plt.ylabel('tip ($)')
plt.show()

sns.swarmplot(x='tip', y='day', data=tips, orient='h')
plt.ylabel('tip ($)')
plt.show()

sns.boxplot(x='day', y='tip', data=tips)
plt.ylabel('tip ($)')
plt.show()

sns.violinplot(x='day', y='tip', data=tips)
plt.ylabel('tip ($)')
plt.tight_layout()
plt.show()

sns.violinplot(x='day', y='tip', data=tips, inner=None, color='lightgray')
sns.stripplot(x='day', y='tip', data=tips, jitter=True, size=4)
plt.ylabel('tip ($)')
plt.show()


sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
plt.show()

sns.pairplot(tips)
plt.show()

sns.pairplot(tips, hue='sex')
plt.show()


sns.heatmap(tips)
plt.title('HEATMAP')
plt.show()


sns.jointplot(x='hp', y='mpg', data=auto)
plt.show()

sns.jointplot(x='hp', y='mpg', data=auto, kind='hex')
plt.show()


print(auto.head())
sns.pairplot(auto)
plt.show()


print(auto.head())
sns.pairplot(auto, kind='reg', hue='origin')
plt.show()

sns.heatmap(auto)
plt.show()




sns.lmplot(x='weight', y='hp', data=auto)
plt.show()

sns.residplot(x='hp', y='mpg', data=auto, color='green')
plt.show()


plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

sns.regplot(x='weight', y='mpg', data=auto,
            scatter=None, color='blue', label='order 1')

sns.regplot(x='weight', y='mpg', data=auto, scatter=None,
            order=2, color='green', label='order 2')

plt.legend(loc='upper right')
plt.show()

sns.lmplot(x='weight', y='hp', data=auto, hue='origin', palette='Set1')
plt.show()

sns.lmplot(x='weight', y='hp', data=auto, row='origin')
plt.show()


plt.subplot(2, 1, 1)
sns.stripplot(x='cyl', y='hp', data=auto)

plt.subplot(2, 1, 2)
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=3)

plt.show()


plt.subplot(2,1,1)
sns.swarmplot(x='cyl', y='hp', data=auto)

plt.subplot(2,1,2)
sns.swarmplot(x='hp', y='cyl', data=auto, hue='origin', orient='h')

plt.show()

plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='hp', data=auto)

plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='hp', data=auto, color='lightgray', inner=None)
sns.stripplot(x='cyl', y='hp', data=auto, jitter=True, size=1.5 )

plt.show()
