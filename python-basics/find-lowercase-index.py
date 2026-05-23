# Setup basic cipher variables
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Chain methods: get the first character, convert it to lowercase, and find its index
# 'H' becomes 'h', which exists in the alphabet string at index 7
index = alphabet.find(text[0].lower())
# Output the correct index
print(index)
