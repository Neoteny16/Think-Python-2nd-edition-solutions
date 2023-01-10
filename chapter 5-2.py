def check_fermat(a, b, c, n):
    """checks if fermat's last theory is legit"""
    if a**n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
        return
    print("No, that doesn't work.")

def fermat():
    """Takes user input to check if fermats theory is legit"""
    print("Lets check if Fermat's last theory is valid")
    a = int(input("Type values for a:\n"))
    b = int(input("Type values for b:\n"))
    c = int(input("Type values for c:\n"))
    n = int(input("Type values for n, must be bigger than 2:\n"))
    if n <= 2:
        n = int(input("Type values for n, must be bigger than 2:\n"))
    check_fermat(a,b,c,n)


# check_fermat(2,4,6,3)

fermat()