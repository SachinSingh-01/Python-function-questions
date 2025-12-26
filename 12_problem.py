'''Write a function factorial(n) that:
Returns the factorial of a number
Use a loop, not recursion'''
def factorial(n):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i+=1
    return fact
result=factorial(4)  
print(result)