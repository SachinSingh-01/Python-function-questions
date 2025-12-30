'''Write a function is_palindrome(s) that:
Returns True if the string is a palindrome
Returns False otherwise
Ignore case.'''
def is_palindrome(s):
    s=s.lower()
    reverse_string=""
    original=s
    for ch in s:
        reverse_string=ch+reverse_string
    if original==reverse_string:
        return True
    else:
        return False
print(is_palindrome("madam"))
print(is_palindrome("sachin"))
print(is_palindrome("mom"))

