import string
import requests
import json

# request encrypted flag
r = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
r.encoding
res = (r.text[15:79])
# print(res)

# request plaintext/decrypting flag
endpointdec = 'http://aes.cryptohack.org/block_cipher_starter/decrypt/' + res
dec = requests.get(endpointdec)
dec.encoding
res1 = (dec.text[14:78])
# print(res1)

by = bytes.fromhex(res1)
finalres = by.decode()
print(finalres)