def countdown(n):
    if n <= 0:
        print('Blastoff!')
        print('returns', n)
    else:
        print(n)
        countdown(n-1)
        print('returns', n)

# countdown(3)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


# print_n('eliso', 3)

def do_n(f, s, n2, n):
    # prints a func given n times. assignment requires to be able to call every function n times, but seems impossible without for loop(googl confirmed as well)
    if n <= 0:
        return
    f(s,n2)
    print(n)
    do_n(f, s, n2, n-1)
do_n(print_n, 'eliso', 3, 5)
do_n(print, 'my D', 3, 5)










