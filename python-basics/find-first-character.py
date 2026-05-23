# Define variables for text, shift, and alphabet reference
text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Find the index of the first character of 'text' (which is 'H') in the alphabet
# Since 'H' is uppercase and alphabet is lowercase, this returns -1 (not found)
# This perfectly demonstrates that Python is case-sensitive
alphabet.find(text[0])
