import math
def area(radius):
    a = math.pi * radius ** 2
    return a
    # or
    # return math.pi * radius ** 2

print(area(28))
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

print(absolute_value(0))

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

print(compare(2,2))

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result


print(distance(1,2,4,6))

def hypotenuse(x, y):
    return math.sqrt(x**2 + y**2)

print(hypotenuse(3, 4))

def circle_area(xc, yc, xp, yp):
    # radius = distance(xc, yc, xp, yp)
    # result = area(radius)
    # return result
    # or
    return area(distance(xc, yc, xp, yp))

print(circle_area(1,2,4,6))

def is_divisible(x, y):
    # if x % y == 0:
    #     return True
    # else:
    #     return False
    #or
    return x % y == 0

print(is_divisible(4, -9))
if is_divisible(4, 2):
    print("Yes, very divisible")

def is_between(x, y, z):
    print(x<=y)
    return x <= y <= z
print(is_between(0,0.5,1))

def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)



def factorial(n):
    ''' factroial with the indentation of output
    
    '''
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if not isinstance(n, int):
        print('Factorial is only defined for integers')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers')
        return None
    elif n == 0:
        return 1
    else:
        res = n * factorial(n-1)
        print(space, 'returning', res)
        return res

print(factorial(5))

def fibonacci(n):
    ''' calculate n-th value of fibonacci
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(3))







