#Processing data in chunks

with open('world_dev_ind.csv') as file:
    file.readline()
    counts_dict = {}
    for j in range(0, 1000):
        line = file.readline().split(',')
        first_col = line[0]
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

print(counts_dict)



