import requests
import hashlib
import sys

# request encrypted flag
r = requests.get('http://aes.cryptohack.org/passwords_as_keys/encrypt_flag/')
r.encoding
res = (r.text[15:79])
# print(res)

# brute forcing the key to find the plaintext, unfortunately not yet finished, i still dont know the flag :(
with open('Tugas5/words', 'r') as f:
    for words in f:
        words = words.strip()

        key = hashlib.md5(words.encode('utf-8')).hexdigest()

        # request plaintext/decrypting flag
        endpointdec = 'http://aes.cryptohack.org/passwords_as_keys/decrypt/' + res + '/' + key
        dec = requests.get(endpointdec)
        dec.encoding
        res1 = (dec.text[14:78])
        # print(res1)

        by = bytes.fromhex(res1)
        print(by)
        if by.startswith('crypto{'.encode()):
            print("key is %s" % words)
            print(by.decode('utf-8'))
            sys.exit(0)
        print(words)
