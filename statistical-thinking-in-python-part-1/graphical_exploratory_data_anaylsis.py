import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

df_swing = pd.read_csv('2008_swing_states.csv')
iris = pd.read_csv('iris.csv')

print(df_swing[['state', 'county', 'dem_share']])
"""
bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

_ = plt.hist(df_swing['dem_share'], bins=bin_edges)
_ = plt.xlabel('Percent of Vote For Obama')
_ = plt.ylabel('number of Counties')
#_ = plt.show()
"""

versicolor_petal_length = iris['versicolor']

"""
# Set default Seaborn style
sns.set()

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot the histogram
plt.hist(versicolor_petal_length, bins=n_bins)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()

"""

#bee swarm plots
"""
_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)
_ = plt.xlabel('state')
_ = plt.ylabel('percent of vote for Obama')
plt.show()
"""
df = iris
print(df)
"""
# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')
# Show the plot
plt.show()


x = np.sort(df_swing['dem_share'])

y = np.arange((1, len(x) + 1) / len(x))

_ = plt.plot(x, y, marker='.', linestyle='none')

_ = plt.xlabel('percent of vote for obama')
_ = plt.ylabel('ECDF')

plt.margins(0.02)
plt.show()


"""

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

"""
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
_ = plt.xlabel('percentage')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()


# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)


# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set, marker='.', linestyle='none')
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
_ = plt.plot(x_virg, y_virg, marker='.', linestyle='none')

# Make nice margins
_ = plt.margins(0.02)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()

"""

