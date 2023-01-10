def is_power(a,b):
    '''
    checks if number a is a power of number b(e.g: 16 is a power of 2)
    '''
    print(a)
    if a == 1:
        return True
    if a % b != 0:
        return False
    return is_power(int(a/b), b)

print(is_power(6,3))