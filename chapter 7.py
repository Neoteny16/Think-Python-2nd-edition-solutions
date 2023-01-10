def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!!!')


countdown(5)

def sequence(n):
    '''
    Collatz conjecture - no matter what input int, it goes down to 1.
    '''
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n)

# def sequence(n):
#     '''
#     Collatz conjecture for negative integers- no matter what input int it goes down to -1.
#     '''
#     while n != -1:
#         print(n)
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = n * 3 - 1
#     print(n)

# sequence(129)

def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1
        

print_n("otar", 10)

# while True:
#     line = input('(write done to exit)>>> ')
#     if line == 'done':
#         print('exited')
#         break
#     print('You wrote:', line)
a = 9
x = 4
epsilon = 0.0000001
while True:
    '''
    Newtonian method of computing sqr root of a
    '''
    print(x)
    y = (x + a / x) / 2
    # if y == x:
    #     break
    if abs(y - x) < epsilon:
        break
    x = y




def comp9(n):
    '''
    computes n times nine
    n - single digit int.
    '''
    return int(str(n-1) + str(10-n))
print(comp9(4))