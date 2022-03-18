# XOR Properties Cryptohack - Windy Arya - 5027201071
import binascii
from pwn import xor

hkey1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
hkey21 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
hkey32 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
hflagkey123 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

bkey1 = bytes.fromhex(hkey1)
bkey21 = bytes.fromhex(hkey21)
bkey32 = bytes.fromhex(hkey32)
bfk123 = bytes.fromhex(hflagkey123)

key2 = xor(bkey1, bkey21)
key3 = xor(key2, bkey32) 

key123 = xor(bkey21, key3)

flag = xor(bfk123, key123)

print(flag.decode('utf-8'))