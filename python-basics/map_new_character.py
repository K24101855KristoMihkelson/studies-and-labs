# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Iterate through the text, converting it to lowercase first
for char in text.lower():
    # Find the original index of the character
    index = alphabet.find(char)
    print(char, index)
    # Calculate the new shifted index
    new_index = index + shift
    # Map the new index back to a character in the alphabet
    new_char = alphabet[new_index]
