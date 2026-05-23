# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Find the index of 'h' and output it (returns 7)
index = alphabet.find(text[0].lower())
print(index)
# Retrieve the character at the found index and print it
# This verifies that we successfully extracted 'h' before applying the shift
shifted = alphabet[index]
print(shifted)
