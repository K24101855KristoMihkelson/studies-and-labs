# Setup basic cipher variables
text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Initialize an empty string to store the final encrypted result
encrypted_text = ''
# Iterate through the text, converting it to lowercase first
for char in text.lower():
    # Control flow: Check if the current character is a space
    # (Note: Added the space back between the quotes)
    if char == ' ':
        # If true, append the space directly
        encrypted_text += char
    else:
        # Find the original index of the letter
        index = alphabet.find(char)
        # Calculate the new shifted index using the modulo operator
        # This mathematically handles the wrap-around for letters at the end of the alphabet
        new_index = (index + shift) % 26
        # Append the successfully shifted character
        encrypted_text += alphabet[new_index]
    # Output the ongoing accumulation of the encrypted text
    print('char:', char, 'encrypted text:', encrypted_text)
