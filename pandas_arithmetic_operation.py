import pandas as pd

from glob import glob


def weather():
    weather = pd.read_csv('pittsburgh2013.csv', index_col='Date', parse_dates=True)

    print(weather.loc['2013-7-1':'2013-7-7', 'PrecipitationIn'])

    precipitation_cm = weather.loc['2013-7-1':'2013-7-7', 'PrecipitationIn'] * 2.54

    print(precipitation_cm)
    
    week1_range = weather.loc['2013-07-01':'2013-07-07', 
        ['Min TemperatureF', 'Max TemperatureF']]

    print(week1_range)

    week1_mean= weather.loc['2013-07-01':'2013-07-07', 'Mean TemperatureF']

    print(week1_mean)

    mean_res = week1_range.divide(week1_mean, axis='rows')

    print(mean_res)

    percent_change = week1_mean.pct_change() * 100
    print(percent_change)

    temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]
    temps_c = (temps_f - 32) * 5/9
    temps_c.columns = temps_c.columns.str.replace('F', 'C')

    print(temps_c.head())   


#weather()




def medals():
    bronze = pd.read_csv('bronze_top5.csv', index_col=0)
    silver = pd.read_csv('silver_top5.csv', index_col=0)
    gold = pd.read_csv('gold_top5.csv', index_col=0)

    print(gold)

    bns = bronze + silver
    print(bns)

    bns = bronze.add(silver, fill_value=0)
    print(bns)

    bsg = bronze + silver + gold
    print(bsg)

    bsg = bronze.add(silver, fill_value=0).add(gold, fill_value=0)
    print(bsg)
    bronze = pd.read_csv('bronze_top5.csv', index_col=0)
    silver = pd.read_csv('silver_top5.csv', index_col=0)
    gold = pd.read_csv('gold_top5.csv', index_col=0)

    print(gold)

    bns = bronze + silver
    print(bns)

    bns = bronze.add(silver, fill_value=0)
    print(bns)

    bsg = bronze + silver + gold
    print(bsg)

    bsg = bronze.add(silver, fill_value=0).add(gold, fill_value=0)
    print(bsg)

#medals()

def gdp():
    gdp = pd.read_csv('GDP.csv', parse_dates=True, index_col='DATE')

    post2008 = pd.DataFrame(gdp['2008':])

    print(post2008.tail(8))

    yearly = post2008.resample('A').last()

    # Print yearly
    print(yearly)

    # Compute percentage growth of yearly: yearly['growth']
    yearly['growth'] = yearly.pct_change() * 100

    # Print yearly again
    print(yearly)


#gdp()

sp500 = pd.read_csv('sp500.csv', parse_dates=True, index_col='Date')

exchange = pd.read_csv('exchange.csv', parse_dates=True, index_col='Date')

dollars = sp500[['Open','Close']]
print(dollars.head())

pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')

print(pounds.head())    
