import pandas as pd

from glob import glob

def weather():
    weather1 = pd.read_csv('pittsburgh2013.csv', index_col='Date')
    print(weather1.head())

    weather2 = weather1.sort_index()

    print(weather2.head())

    weather3 = weather1.sort_index(ascending=False)

    print(weather3.head())

    weather4 = weather1.sort_values('Max TemperatureF')

    print(weather4.head())

    year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    weather2 = weather1.reindex(year)

    print(weather2)

    weather3 = weather1.reindex(year).ffill()

    print(weather3)

#weather() 

def baby_names():

        
    names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
    names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'], index_col=(0,1))



    common_names = names_1981.reindex(names_1881.index)

    print(common_names.shape)

    common_names = common_names.dropna()    

    print(common_names.shape)


baby_names()

