'''Write a function is_palindrome(n) that:
Returns True if the number is a palindrome
Returns False otherwise
Ignore case.'''
def is_palindrome(n):
    original=n
    temp=0
    while n>0:
        digit=n%10
        temp=(temp*10)+digit
        n=n//10
    if original==temp:
        print("Yes palindrome")
    else:
        print("No not a palindrome")
is_palindrome(121)