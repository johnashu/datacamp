import pandas as pd
import matplotlib.pyplot as plt

def plot_pop(filename, country_code):
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)
    data = pd.DataFrame()
    
    for df_urb_pop in urb_pop_reader:
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])
        pops_list = list(pops)

        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]
        data = data.append(df_pop_ceb)

        data.plot(kind='scatter', x='Year', y='Total Urban Population')
        plt.show()
fn = 'ind_pop_data.csv'

plot_pop(fn, 'CEB')
plot_pop(fn, 'ARB')


