import pandas as pd
#Processing large amounts of Twitter data

counts_dict = {}

for chunk in pd.read_csv("tweets2.csv", chunksize=10):
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
print(counts_dict)


#Extracting information for large amounts of Twitter data

def count_entries(csv_file, c_size, colname):
    """ Return a dictionary with counts of occurrences as value for each key."""
    counts_dict1 = {}

    for chunk in pd.read_csv(csv_file, chunksize=c_size):
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    return counts_dict

result_counts = count_entries('tweets2.csv', 10, 'lang')
print(result_counts)
