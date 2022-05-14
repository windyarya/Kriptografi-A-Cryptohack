from traceback import print_tb


plain = 12
e = 65537
p = 17
q = 23

n = p * q
print(pow(plain, e, n))