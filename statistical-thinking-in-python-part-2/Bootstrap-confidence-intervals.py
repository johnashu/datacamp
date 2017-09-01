import pandas as pd

#ecdf
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n
    return x, y

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

michelson_speed_of_light = pd.read_csv('michelson_speed_of_light.csv')

bs_sample = np.random.choice(michelson_speed_of_light, size=100)


