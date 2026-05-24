# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Iterate through the text, converting it to lowercase first
for char in text.lower():
    # Find the index of the character in the alphabet
    index = alphabet.find(char)
    # Output the character and its index
    print(char, index)
