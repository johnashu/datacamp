import pandas as pd

name_2_check = 'Rosie'

def baby_name_chack(name):
    names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'])
    names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'])

    names_1881['year'] = 1881
    names_1981['year'] = 1981


    combined_names = names_1881.append(names_1981, ignore_index=True)

    print(names_1981.shape)
    print(names_1881.shape)
    print(combined_names.shape)

    print(combined_names.loc[combined_names['name'] == name])

baby_name_check(name_2_check)