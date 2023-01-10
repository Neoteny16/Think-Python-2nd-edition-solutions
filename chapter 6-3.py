def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


print(middle(''))



# solution

def is_palindrome(word):
    ''' 
    returns True if word is a palindrome(example: redivider)
    '''
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('polo5olop'))







