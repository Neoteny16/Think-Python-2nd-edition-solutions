def do_twice(f,v):
    f(v)
    f(v)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)
do_twice(print_twice, 'spam1')
do_four(print_twice, 'spam2')