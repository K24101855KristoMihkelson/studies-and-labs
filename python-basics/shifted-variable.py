# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Find the index of 'h' in the alphabet (returns 7)
index = alphabet.find(text[0].lower())
print(index)
# Retrieve the character from the alphabet using the found index
# This prepares the variable for the upcoming shift addition
shifted = alphabet[index]
