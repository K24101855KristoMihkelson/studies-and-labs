# Setup basic cipher variables
text = 'Hello World'
# Successfully reassign the text variable
text = 'train'
# Attempting to mutate a string (This will intentionally cause a TypeError)
# Strings in Python are immutable
text[0] = 't'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Iterate through the text, converting it to lowercase first
for char in text.lower():
    # Find the original index of the character
    index = alphabet.find(char)
    print(char, index)
    # Calculate the new index by applying the shift value
    new_index = index + shift
