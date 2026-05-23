# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Iterate through the text
for char in text:
    # Strictly assign the find method to the index variable as requested
    index = alphabet.find(char)
    print(char)
    print(index)
