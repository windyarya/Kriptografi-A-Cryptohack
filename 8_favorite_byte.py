# Favorite Bytes Cryptohack - Windy Arya - 5027201071
import binascii

text = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

btext = bytearray.fromhex(text)

for i in range(256):
    result = ''
    for n in btext:
        result += chr(n^i)
    
    if (result.startswith('crypto')):
        print(result)
