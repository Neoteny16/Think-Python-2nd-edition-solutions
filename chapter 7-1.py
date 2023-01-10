import math, random

def mysqrt(a):
    '''
    Newtonian method of computing sqr root of a
    a - int which sqrt needs to be find
    x - estimate number choosed randomly
    '''
    x = random.randint(1, a)
    while True:
        epsilon = 0.0000001
        y = (x + a / x) / 2
        # if y == x:
        #     break
        if abs(y - x) < epsilon:
            return y
        x = y

# print(mysqrt(mysqrt(81)))


def test_square_root(a, b):
    '''
    print table of comparison of self made sqrt and math.sqrt and difference between them
    a, b - int. starting and end point, range
    '''
    space = ' '
    print('a ' + 'mysqrt(a)' + space * 10 + 'math.sqrt(a)' + space * 7 + 'diff')
    print('- ' + '---------' + space * 10 + '------------' + space * 7 + '----')
    
    while a < b:
        mysq = mysqrt(a)
        mathsq = math.sqrt(a)
        space = ' '
        print(str(a) + ' ' + str(mysq) + space * (19 - len(str(mysq))) + str(mathsq) + space * (19 - len(str(mathsq))) + str(abs(mysq - mathsq)))
        a = a + 1


test_square_root(1, 1000)