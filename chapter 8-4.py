# parameter is a string

def any_lowercase1(s):
    """
    Checks if first char in s is lowercase, T or F
    """
    for c in s:
        if c.islower():
            return True 
        else:
            return False
            
def any_lowercase2(s):
    """
    Broken, returns str 'True' no matter what input, because 'c'.islower() is always True
    """
    for c in s:
        if 'c'.islower():  
            return 'True'
        else:
            return 'False'
            
def any_lowercase3(s):
    """
    Returns True or False depending on last char in str. True if last char is lower. 
    """
    for c in s:
        flag = c.islower() 
    return flag
    
def any_lowercase4(s):
    """
    If any of the char is lowercase returns True
    In the beginning flag is false, but as the first lowercase comes in flag will stay True,
    according to truth table for or relational operator
    """
    flag = False
    for c in s:
        flag = flag or c.islower() 
    return flag
    
def any_lowercase5(s):
    """
    Returns false if any of the character is uppercase, otherwise it gets through loop and
    returns True.
    """
    for c in s:
        if not c.islower():
            return False 
    return True


print(any_lowercase1('BANAnA'))
print(any_lowercase2('BananA'))
print(any_lowercase3('BANAna'))
print(any_lowercase4('BANAnA'))
print(any_lowercase5('fasfQwe'))