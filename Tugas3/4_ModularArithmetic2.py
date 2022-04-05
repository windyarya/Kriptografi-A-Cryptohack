def fermat_theorem_mod(base, exp, prime):
    if exp == prime:
        return base
    elif exp + 1 == prime and base % prime != 0:
        return 1
    else:
        return -1;
        
print(fermat_theorem_mod(273246787654, 65536, 65537))