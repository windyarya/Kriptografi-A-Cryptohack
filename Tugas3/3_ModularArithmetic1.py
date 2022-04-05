# 11 ≡ x mod 6
# 8146798528947 ≡ y mod 17

x = 11 % 6
y = 8146798528947 % 17

#The smaller integer is the flag
if x > y:
    print(y)
else:
    print(x)