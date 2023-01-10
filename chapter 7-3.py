import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def estimate_pi():
    '''
    computes estimation of pi by Srinivasa Ramanujan
    '''
    k = 0
    consta = 2 * math.sqrt(2) / 9801
    sum = 0
    while True:
        # sum += (factorial(4 * k) * (1103 + 26390 * k)) / ((factorial(k) ** 4) * (396 ** (4 * k))) 
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        
        sum += num/den

        term = consta * num/den
        if abs(term) < 1e-15:
            break
        k += 1
    return 1 / (consta * sum)

print(estimate_pi())
print(abs(math.pi - estimate_pi()))