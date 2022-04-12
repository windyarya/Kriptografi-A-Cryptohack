import requests
import json
import binascii
from PIL import Image

url = 'http://aes.cryptohack.org/bean_counter/encrypt/'

def xor_hex(a, b):
    temp = int(a, 16) ^ int(b, 16)
    res = hex(temp)[2:].zfill(2)
    return res

def encrypted():
    r = requests.get(url)
    enc = r.json()['encrypted']
    return enc

def decrypted(encm, key):
    dec = ''
    t = 0
    for i in range(0, len(encm), 2):
        temp =xor_hex(encm[i:i+2], key[t:t+2])
        t += 2
        if (t >= len(key)):
            t = 0
        dec += temp
    d = bytes.fromhex(dec)
    with open('Tugas6/beancounter.png', 'wb') as f:
        f.write(d)

enc = encrypted()
encpic = binascii.unhexlify(enc)
pngheader = '89504e470d0a1a0a0000000d49484452'

# first 11 bytes of key
print(len(enc), len(enc) % 32)

key1 = enc[:32]
key = ''
for i in range(0, len(key1), 2):
	temp = xor_hex(key1[i:i+2], pngheader[i:i+2])
	key += temp

# print(key)
decrypted(enc, key)
im = Image.open(r"Tugas6/beancounter.png")
im.show()