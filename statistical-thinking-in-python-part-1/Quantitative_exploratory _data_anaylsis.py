import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y



    



df = pd.read_csv('2008_all_states.csv')
df_swing = pd.read_csv('2008_swing_states.csv')
iris = pd.read_csv('iris.csv')

print(df.head())

dem_share = df[['dem_share', 'state']]
dem_share_PA = dem_share.loc[dem_share['state'] == 'PA']
dem_share_UT = dem_share.loc[dem_share['state'] == 'UT']


print(dem_share_UT)

print(np.mean(dem_share_PA))

print(np.median(dem_share_UT.dem_share))


percentile = np.percentile(df_swing['dem_share'], [25, 50, 75])
print(percentile)

"""
_ = sns.boxplot(x=df['east_west'], y=df['dem_share'])
_ = plt.xlabel('region')
_ = plt.ylabel('percent of vote for Obama')
plt.show()
"""

def std_deviation(data):
    """ A function to calculate the Standard Deviation of Data by caclulating the Square Root of The Variance"""
    def variance():
        """ Function to calculate the Variance of data by calculating the average of the squared differnces from the mean"""
        mean_av = np.mean(data)
        return mean_av
    
    print(variance())

maf_std_dev = std_deviation(dem_share_PA)

print(maf_std_dev)

# variance

#print(np.var(dem_share))


"""

#NEED THE FULL IRIS DATASET.. WITH PETAL LENGTHS.. 

# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)

# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
plt.margins(0.02)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
         linestyle='none')

# Show the plot
plt.show()


# Create box plot with Seaborn's default settings
sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')


# Show the plot
plt.show()


"""
# Array of differences to mean: differences


# Square the differences: diff_sq


# Compute the mean square difference: variance_explicit


# Compute the variance using NumPy: variance_np


# Print the results
