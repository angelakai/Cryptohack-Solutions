import base64
a='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

#Decoding hex to bytes
decode=bytes.fromhex(a)

#Encoding it to basee 64
encode=base64.b64encode(decode)

print(encode)
