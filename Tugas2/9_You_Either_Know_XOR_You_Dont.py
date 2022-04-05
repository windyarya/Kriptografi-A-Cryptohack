# You either know, XOR you don't Cryptohack - Windy Arya - 5027201071
from pwn import xor
import binascii

text = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# pkey = xor(text[:7], "crypto{") 
# print(pkey.decode()) => myXORke --> myXORkey
pkey = "myXORkey"


key = (pkey * (len(text)//len(pkey)+1))[:len(text)]

flag = xor(text, key)

print(flag.decode('utf-8'))