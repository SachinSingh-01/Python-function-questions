'''Write a function is_even(n) that:
Prints "Even" if the number is even
Prints "Odd" if the number is odd
Call the function with any number.'''
def is_even(n):
    if n%2==0:
        print("Even number")
    else:
        print("Odd number")
is_even(3)