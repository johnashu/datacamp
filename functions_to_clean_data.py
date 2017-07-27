import pandas as pd
import re

from numpy import NaN

tips = pd.read_csv('tips.csv')


def recode_sex(sex_value):
    """will recode 'Male' to 1, 'Female' to 0, and return np.nan 
    for all entries of 'sex' that are neither 'Male' nor 'Female'"""
    if sex_value == 'Male':
        return 1
    elif sex_value == 'Female':
        return 0
    else:
        return np.nan

tips['sex_recode'] = tips.sex.apply(recode_sex)
print(tips.head())


#Lambda Functions

tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])

print(tips.head())