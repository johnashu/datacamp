import pandas as pd
import matplotlib.pyplot as plt

# Writing a generator to load data in chunks
def read_large_file(file_object):
    """A generator to read a large file lazily!!"""
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data


with open('world_dev_ind.csv') as file:
    gen_file = read_large_file(file)
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

# process the file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset

counts_dict = {}

with open('world_dev_ind.csv') as file:
    for line in read_large_file(file):
        row = line.split(',')
        first_col = row[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

print(counts_dict)


"""
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)
print(next(df_reader))
print(next(df_reader))
"""
#Writing an iterator to load data in chunks 

urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
print(df_urb_pop.head())

df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'],
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)
df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]

df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()


urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
data = pd.DataFrame()

for df_urb_pop in urb_pop_reader:
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])
    pops_list = list(pops)
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]
    data = data.append(df_pop_ceb)

data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()


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


