# Setup basic cipher variables
text = 'Hello Zaira'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Initialize an empty string to store the final encrypted result
encrypted_text = ''
# Iterate through the text, converting it to lowercase first
for char in text.lower():
    # Control flow: Check if the current character is a space
    if char == ' ':
        # If true, append the space directly
        encrypted_text += char
    else:
        # Find the original index of the letter
        index = alphabet.find(char)
        # Calculate the new shifted index dynamically using len() and modulo
        # This prevents hardcoding the number 26 and allows the alphabet length to change
        new_index = (index + shift) % len(alphabet)
        # Append the successfully shifted character
        encrypted_text += alphabet[new_index]
    # Output the ongoing accumulation of the encrypted text
    print('char:', char, 'encrypted text:', encrypted_text)
