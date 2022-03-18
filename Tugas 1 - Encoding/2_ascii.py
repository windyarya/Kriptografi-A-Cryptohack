# ASCII Cryptohack - Windy Arya - 5027202071
from os import sep

acode = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
atext = []

for i in acode:
    atext.append(chr(i))

print(*atext, sep="")