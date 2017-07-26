lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

def get_lengths(input_list):
    """Generatot function that yields the length of the strings in input list."""
    for person in input_list:
        yield len(person)

for value in get_lengths(lannister):
    print(value)