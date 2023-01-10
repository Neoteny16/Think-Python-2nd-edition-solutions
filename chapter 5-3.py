def is_triangle(a, b, c):
    """Check if these lengths are valid to create triangle,
    if length of one side is bigger than sum of other two, you can't
    form the triangle"""
    if a > b + c or b > a + c or c > a + b:
        print("No, you can't form triangle with this lengths.")
    else:
        print("Yes, you can form triangle!")

is_triangle(3,2,1)

def try_triangle():
    """Takes user input to check if fermats theory is legit"""
    print("Lets check if you can make triangle")
    a = int(input("Type length for a:\n"))
    b = int(input("Type length for b:\n"))
    c = int(input("Type length for c:\n"))   
    is_triangle(a,b,c)

try_triangle()