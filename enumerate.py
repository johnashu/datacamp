mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pride']

aliases = ['1', '2']

powers = ['3', '4']

mutant_list = list(enumerate(mutants))
print(mutant_list)

# unpack and print in pairs
for index1, value1 in enumerate(mutant_list):
    print(index1, value1)

for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)


mutant_data = list(zip(mutants, aliases, powers))
print(mutant_data)

mutant_zip = zip(mutants, aliases, powers)
print(mutant_zip)

for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

# * and zipm to unzip

