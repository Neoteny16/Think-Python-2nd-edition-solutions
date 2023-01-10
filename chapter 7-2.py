import math
def eval_loop():
    while True:
        line = input('(write done to exit)>>> ')
        if line == 'done':
            print('Last evaluated value:', evaluated)
            break
        evaluated = eval(line)
        print(evaluated)

eval_loop()