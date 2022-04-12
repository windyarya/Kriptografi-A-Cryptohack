import json
import requests
from Crypto.Util.number import bytes_to_long, long_to_bytes

url = 'http://aes.cryptohack.org/flipping_cookie/'
cconfig = 'admin=True;'

def getCookie():
    r = requests.get(url + "get_cookie/")
    cookie = r.json()["cookie"]
    return (cookie)

def check_admin(cookie, iv):
    r = requests.get(url + "check_admin/" + cookie + "/" + iv + "/")
    f = r.json()["flag"]
    return f

cookie = getCookie()
iv = cookie[:32]
co = cookie[32:64]
# print(iv)
# print(co)
desPlain = b'admin=True;'
plain = b'admin=False'

iv2 = [int(iv[i:i+2], 16) for i in range(0, len(iv), 2)]
# print(iv2)

xAdmin = []
for i in range(len(plain)):
    xAdmin.append(plain[i] ^ desPlain[i])

adm = ''
for a, b in zip(xAdmin, plain):
    adm += chr(a ^ b)
# print(adm)

iv3 = ''
for i in range(len(xAdmin)):
    iv3 += hex(xAdmin[i] ^ iv2[i])[2:].zfill(2)

if (len(iv3) == len(xAdmin) * 2):
    iv3 += iv[len(iv3):]

# print(adm)
# print(cconfig)
# print(iv3)
# print(len(iv3) % 32)

if ((adm == cconfig) and (len(iv3) % 32 == 0)):
    print(check_admin(cookie[32:], iv3))