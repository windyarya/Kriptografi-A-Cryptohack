def gcd(a, b):
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b

print(gcd(66528, 52920))