import requests
import time
import string

# encrypting the message
def encrypt(payload):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    r = requests.get(url + payload + '/')
    return r.json()['ciphertext']

# printing block cipher
def print_cipher(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

# initialize the flag
flag = ''
total = 32 - 1
alphabet = '_'+'@'+'{'+'}'+string.digits+string.ascii_lowercase+string.ascii_uppercase

# brute force (again) :)
while True:
    payload = 'a' * (total-len(flag))
    expected = encrypt(payload.encode().hex())
    print('E', '', end='')
    print_cipher(expected, 32)
        
    for c in alphabet: 
        res = encrypt(bytes.hex((payload + flag + c).encode()))
        print(c, '', end='')
        print_cipher(res, 32)
        if res[32:64] == expected[32:64]:
            flag += c
            print(flag)
            break
        time.sleep(1)

    if flag.endswith('}'): 
        break

print(flag)