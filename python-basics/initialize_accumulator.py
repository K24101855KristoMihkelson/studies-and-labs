# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Initialize an empty string to store the final encrypted result
encrypted_text = ''
# Iterate through the text, converting it to lowercase first
for char in text.lower():
    # Find the original index of the character
    index = alphabet.find(char)
    # Calculate the new shifted index
    new_index = index + shift
    # Map the new index back to a character
    new_char = alphabet[new_index]
    # Output the original and encrypted character side-by-side
    print('char:', char, 'new char:', new_char)
