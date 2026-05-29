# Setup basic cipher variables
# Changed text to 'Hello Zaira' to intentionally test an edge case (the letter 'z')
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
        # Calculate the new shifted index
        # LOGICAL BUG: For 'z' (index 25), 25 + 3 = 28.
        # This will cause an IndexError because the alphabet string only goes up to index 25.
        new_index = index + shift
        # Attempt to append the newly shifted character
        encrypted_text += alphabet[new_index]
    # Output the ongoing accumulation of the encrypted text
    print('char:', char, 'encrypted text:', encrypted_text)
