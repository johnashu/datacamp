mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pride']

aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']

powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']



z1 = zip(mutants, powers)
print(*z1)

#reassign due to it being used for print
z1 = zip(mutants, powers)

result1, result2 = zip(*z1)
print(result1 == mutants)
print(result2 == powers)

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1)
print(result2)

