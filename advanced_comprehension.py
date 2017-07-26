
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]

print(new_fellowship)

# dict comprehensions

new_fellowship = {member: len(member) for member in fellowship}

print(new_fellowship)