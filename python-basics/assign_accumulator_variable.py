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
    # Assign the new character to the encrypted_text variable
    # (Note: This currently overwrites the variable in each iteration)
    encrypted_text = alphabet[new_index]
    # Output the original character and the current state of the encrypted_text
    print('char:', char, 'encrypted text:', encrypted_text)
