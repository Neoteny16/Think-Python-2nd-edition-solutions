pal = "redivider"
notpal = "redivision"
def is_palindrome(s):
    """
    Checks if s is palindrome
    """
    return s[::-1] == s

print(is_palindrome(pal))
print(is_palindrome(notpal))