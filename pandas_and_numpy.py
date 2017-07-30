import pandas as pd

df = pd.read_csv('tips.csv')

import numpy as np

np_vals = df.values

np_vals_log10 = np.log10(np_vals)
df_log10 = np.log10(df)

print(type(np_vals), type(np_vals_log10))
print(type(df), type(df_log10))

