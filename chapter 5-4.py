def recurse(n, s):
    """Sums all n>0 numbers(n must be non-negative integer), s must be zero"""
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

# recurse(-1, 0) # RecursionError: maximum recursion depth exceeded in comparison  ... n goes to -infinity and never reaches 0
recurse(3, 0)


