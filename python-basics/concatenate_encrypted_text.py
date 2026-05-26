Python
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
    # Append the new character to the existing encrypted_text string
    encrypted_text = encrypted_text + alphabet[new_index]
    # Output the ongoing accumulation of the encrypted text
    print('char:', char, 'encrypted text:', encrypted_text)
