# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Iterate through the text
for char in text:
    # Find the index of the character in the alphabet
    index = alphabet.find(char)
