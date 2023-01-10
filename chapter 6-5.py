def gcd(a, b):
    '''
    find greatest common divisor of two int.
    '''
    print(a, b)
    if b == 0:
        return a
    remain = a % b
    return gcd(b, remain)

print(gcd(6, 26))