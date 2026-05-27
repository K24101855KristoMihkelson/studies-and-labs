# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Initialize an empty string to store the final encrypted result
encrypted_text = ''
# Iterate through the text, converting it to lowercase first
for char in text.lower():
    # If the character is a space, append it directly to the result
    if char == ' ':
        encrypted_text += char
    # LOGICAL BUG: Because there is no 'else' statement, the code continues to run.
    # It will find the space index (-1), shift it, and append 'c' right after the space.
    index = alphabet.find(char)
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    # Output the ongoing accumulation of the encrypted text
    print('char:', char, 'encrypted text:', encrypted_text)
