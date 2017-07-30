import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')


# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['total_bill']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['tip']
df[column_list2].plot()
plt.show()

column_list3 = ['size']
df[column_list3].plot()
plt.show()

column_list4 = ['fraction']
df[column_list4].plot()
plt.show()