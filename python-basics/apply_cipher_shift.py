# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Iterate through the text, converting it to lowercase first
for char in text.lower():
    # Find the original index of the character
    index = alphabet.find(char)
    print(char, index)
    # Calculate the new index by applying the shift value
    new_index = index + shift
