from pwn import *

text = "label"
word = ""

#XOR each character in "label" with 13 and store the result in 'text'
for char in text:
    xor_result = ord(char) ^ 13
    word += chr(xor_result)

print(word)
