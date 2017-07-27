import pandas as pd
import re
import pandas as pd
import numpy as np
from numpy import NaN

import matplotlib.pyplot as plt

# check data types dtype
gapminder = pd.read_csv('gapminder.csv')

assert pd.notnull(gapminder.country).all()
assert pd.notnull(gapminder.year).all()
gapminder = gapminder.dropna(how='any')
print(gapminder.shape)