from pwn import *
key1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
key1_2='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2_3='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
key_flag='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf' 

#XOR key1_2 with key1 to obtain key2
key2=xor(bytes.fromhex(key1_2),key1)

#XOR key2_3 with key2 to obtain key3
key3=xor(bytes.fromhex(key2_3),key2)

#XOR key1 with key2_3 to obtain key4
key4=xor(key1,bytes.fromhex(key2_3))

#XOR the encrypted flag with key4 to obtain the original flag
flag=xor(bytes.fromhex(key_flag),key4)
print(flag)
