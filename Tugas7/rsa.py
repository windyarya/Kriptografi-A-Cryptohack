import random

def isPrime(a):
    if (a < 2 or a % 2 == 0):
        return False
    for n in range (2, a):
        if (a % n == 0):
            return False
    return True

def gcd(a, b):
    while (b != 0):
        a, b = b, a % b
    return a;

def multiInverse(e, t):
    for x in range(1, t):
        if (((e % t) * (x % t)) % t == 1):
            return x
    return -1

def generateKey(p, q):
    if not (isPrime(p) and isPrime(q)):
        print("Both numbers must be prime.")
        return -1, -1
    elif (p == q):
        print("p and q cannot be equal")
        return -1, -1
    n = p * q
    t = (p-1) * (q-1)

    e = random.randrange(1, t);

    g = gcd(e, t)
    while (g != 1):
        e = random.randrange(1, t)
        g = gcd(e, t)
    
    d = multiInverse(e, t)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    # print(key, n)
    cipher = []
    for char in plaintext:
        temp = (ord(char) ** key) % n
        cipher.append(temp)
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = []
    # print(ciphertext)
    for char in ciphertext:
        # type(char)
        # print(char)
        temp = chr((char ** key) %n)
        plain.append(temp)
    return plain

x, y = input("Enter two prime number (separate with space): ").split()
x = int(x)
y = int(y)
public, private = generateKey(x, y)
if (public != -1 and private != -1):
    print ("Public key :", public ,"Private key:", private)
    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(private, message)
    print ("Encrypted message:", ''.join(map(lambda x: str(x), encrypted_msg)))
    decrypted_msg = decrypt(public, encrypted_msg)
    print ("Decrypted message:", ''.join(decrypted_msg))
    # print (decrypt(public, encrypted_msg))
