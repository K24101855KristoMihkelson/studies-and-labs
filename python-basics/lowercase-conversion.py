# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Find the index of the uppercase 'H' (returns -1)
index = alphabet.find(text[0])
print(index)
# Convert the text to lowercase to ensure characters match the alphabet string
print(text.lower())
