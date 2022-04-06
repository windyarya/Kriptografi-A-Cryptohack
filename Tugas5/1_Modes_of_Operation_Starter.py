import requests

# request encrypted flag
r = requests.get('http://aes.cryptohack.org/block_cipher_starter/encrypt_flag/')
res = r.json()['ciphertext']
# print(res)

# request plaintext/decrypting flag
endpointdec = 'http://aes.cryptohack.org/block_cipher_starter/decrypt/' + res
dec = requests.get(endpointdec)
res1 = dec.json()['plaintext']
# print(res1)

by = bytes.fromhex(res1)
finalres = by.decode()
print(finalres)