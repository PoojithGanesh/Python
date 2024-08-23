#Python program to create and display all combinations of letters selecting each letter from different key in a dictionary
letter_dict = {
    'A': ['a', 'b'],
    'B': ['d', 'e'],
}

for a in letter_dict['A']:
    for b in letter_dict['B']:
        print(a + b)
