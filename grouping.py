
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = 'pennsylvania2012_turnout.csv'


election = pd.read_csv(filename, index_col='county')

results = election[['winner', 'total', 'voters']]

print(election.groupby('winner').count())

print(election.groupby('winner')[['Obama']].sum())

print(election.groupby(['winner', 'county']).mean())

print(election['winner'].unique())


titanic = pd.read_csv('titanic.csv')

by_class = titanic.groupby('pclass')
count_by_class = by_class['survived'].count()
print(count_by_class)
by_mult = titanic.groupby(['embarked', 'pclass'])
count_mult = by_mult['survived'].count()
print(count_mult)


"""
INCORRECT CSV FILES..

life_fname = 'life_expectancy_at_birth.csv'
regions_fname = 'gapminder.csv'

life = pd.read_csv(life_fname, index_col='Country')
regions = pd.read_csv(regions_fname, index_col='Country')
life_by_region = life.groupby(regions['region'])
print(life_by_region['2010'].mean())

"""

by_class = titanic.groupby('pclass')
by_class_sub = by_class[['age', 'fare']]
aggregated = by_class_sub.agg(['max', 'median'])
print(aggregated.loc[:, ('age', 'max')])
print(aggregated.loc[:, ('fare', 'median')])




gapminder = pd.read_csv('gapminder1.csv', index_col=['Year', 'region', 'Country'])
by_year_region = gapminder.groupby(level=['Year', 'region'])

def spread(series):
    return series.max() - series.min()

aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

aggregated = by_year_region.agg(aggregator)
print(aggregated.tail(6))



sales = pd.read_csv('sales1.csv', index_col='Date', parse_dates=True)

by_day = sales.groupby(sales.index.strftime('%a'))
units_sum = by_day.agg({'Units':'sum'})
print(units_sum)


auto = pd.read_csv('auto-mpg.csv')

def zscore(series):
    return (series - series.mean()) / series.std()

print(zscore(auto['mpg']).head())

print(auto.groupby('yr')['mpg'].transform(zscore).head())

def zscore_with_year_and_name(group):
    df = pd.DataFrame(
        {'mpg': zscore(group['mpg']),
        'year': group['yr'],
        'name': group['name']})
    return df

print(auto.groupby('yr').apply(zscore_with_year_and_name).head()) 

splitting = auto.groupby('yr')





gapminder_2010 = pd.read_csv('gapminder1.csv', index_col='Country')

from scipy.stats import zscore

standardized = gapminder_2010.groupby('region')['life', 'fertility'].transform(zscore)
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)
gm_outliers = gapminder_2010.loc[outliers]
print(gm_outliers)

by_sex_class = titanic.groupby(['sex', 'pclass'])

def impute_median(series):
    return series.fillna(series.median())

titanic.age = by_sex_class.age.transform(impute_median)
print(titanic.tail(10))



def disparity(gr):
    """ Compute the disparity """
    s = gr['gdp'].max() - gr['gdp'].min()

    z = (gr['gdp'] - gr['gdp'].mean()) / gr['gdp'].std()
    
    return pd.DataFrame({'z(gdp)':z,  'regional spread(gdp)':s})
"""
regional = gapminder_2010.groupby('region')
reg_disp = regional.apply(disparity)
print(reg_disp.loc['United States','United Kingdom','China'])

"""
for group_name, group in splitting:
    avg = group['mpg'].mean()
    print(group_name, avg )


for group_name, group in splitting:
    avg = group.loc[group['name'].str.contains('chevrolet'), 'mpg'].mean()
    print(group_name, avg )


chevy_means = {year:group.loc[group['name'].str.contains('chevrolet'), 'mpg'].mean() for year, group in splitting}

print(chevy_means)

chevy = auto['name'].str.contains('chevrolet')

pnto = auto.groupby(['yr', chevy])['mpg'].mean()
print(pnto)

def c_deck_survival(gr):
    c_passengers = gr['cabin'].str.startswith('C').fillna(False)

    return gr.loc[c_passengers, 'survived'].mean()


by_sex = titanic.groupby('sex')
c_surv_by_sex = by_sex.apply(c_deck_survival)
print(c_surv_by_sex)

sales = pd.read_csv('sales1.csv', index_col='Date', parse_dates=True)

by_company = sales.groupby('Company')
by_com_sum = by_company.Units.sum()
print(by_com_sum)

by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
print(by_com_filt)

under10 = (titanic['age'] < 10).map({True:'under 10', False:'over 10'})

survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)

survived_mean_2 = titanic.groupby([under10, 'pclass'])['survived'].mean()
print(survived_mean_2)