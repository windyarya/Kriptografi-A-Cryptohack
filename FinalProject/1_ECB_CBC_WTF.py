import requests
from Crypto.Util.number import long_to_bytes

URL = "http://aes.cryptohack.org/ecbcbcwtf/"

# request ciphertext/encrypted flag CBC
r = requests.get(URL + "encrypt_flag")
res = r.json()['ciphertext']
iv = res[:32]

flag = ""
# print(res[32:])
# decrypting the flag ECB, decrypt 16bit
for i in range(1,3):
    cipher = res[32*i:32*(i+1)]
    # print(res[32*i:32*(i+1)], cipher)
    plain = requests.get(URL + "decrypt/" + cipher)
    resp = plain.json()['plaintext']
    res1 = hex(int(resp,16) ^ int(iv, 16))[2:]
    print(long_to_bytes(int(res1, 16)))
    flag = flag + res1
    iv = cipher

print(long_to_bytes(int(flag, 16)))