result = (num for num in range(31))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

for value in result:
    print(value)



lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']
lengths = (len(person) for person in lannister)
for value in lengths:
    print(value)

