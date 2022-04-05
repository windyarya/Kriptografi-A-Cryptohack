# Bytes and Big Integers Cryptohack - Windy Arya - 5027201071
from Crypto.Util.number import *

base10_val = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

print((long_to_bytes(base10_val)).decode('utf-8'))