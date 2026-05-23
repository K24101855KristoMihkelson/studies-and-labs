# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Find the index of the first character ('h' is at index 7)
index = alphabet.find(text[0].lower())
print(index)
# Apply the shift by adding it to the current index (7 + 3 = 10)
# Retrieve the new encrypted character from the alphabet ('k')
shifted = alphabet[index + shift]
# Output the shifted character to verify the cipher logic
print(shifted)
