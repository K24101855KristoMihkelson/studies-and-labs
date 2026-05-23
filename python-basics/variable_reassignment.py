# Setup basic cipher variables
text = 'Hello World'
# Successfully reassign the variable to a entirely new string
text = 'Albatross'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Iterate through the reassigned text, converting to lowercase
for char in text.lower():
    # Find the original index of the character
    index = alphabet.find(char)
    print(char, index)
    # Calculate the shifted index
    new_index = index + shift
