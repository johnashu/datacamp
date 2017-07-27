import pandas as pd
import re

from numpy import NaN

df_job = pd.read_csv('job.csv') 
pattern = re.compile('^\$\d*\.\d{2}$')

def diff_money(row, pattern):

    icost = row['Initial Cost']
    tef = row['Total Est. Fee']

    if bool(pattern.match(icost)) and bool(pattern.match(tef)):
        icost = icost.replace("$", "")
        tef = tef.replace("$", "")
        icost = float(icost)
        tef = float(tef)

        return icost - tef
    else:
        return (NaN)
    
df_job['diff'] = df_job.apply(diff_money, axis=1, pattern=pattern)
print(df_job.head())