#Iterating over Iterables (1)

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

for item in flash:
    print(item)

superspeed = iter(flash)

print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))

#Iterating over Iterables (2)

small_value = iter(range(3))

print(next(small_value))
print(next(small_value))
print(next(small_value))

for num in range(3):
    print(num)

googol = iter(range(10 ** 100))

print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))


# Iterators as function arguments

values = range(10, 21)
print(values)

values_list = list(values)
print(values_list)

values_sum = sum(values)
print(values_sum)

