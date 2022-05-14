from math import sqrt

# Use factordb.com for the faster result

def PrimeFactor(n):
    m = n
    while n%2==0:
        n = n//2
    if n == 1:
        return 2
    i = 3
    sqrt = int(m**(0.5))
    last = 0
    while i <= sqrt :
        while n%i == 0:   
            n = n//i
            last = i
        i+=2
    if n> last:
        return n
    else:
        return last

num = 510143758735509025530880200653196460532653147

print(PrimeFactor(num)) 