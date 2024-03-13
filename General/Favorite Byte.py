from pwn import *

text = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

#Iterate through all keys
for i in range(256):
    #XOR the text with the current key
    flag = xor(text, i)
    #Check if "crypto{" in bytes is present in the decrypted result
    if bytes("crypto{", 'utf-8') in flag:
        #Print decoded flag and exit the loop
        print(flag.decode('utf-8'))
        break
