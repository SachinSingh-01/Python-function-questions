'''Write a function sum_digits(n) that:
Takes an integer
Returns the sum of its digits'''
def sum_digits(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    return total
result=sum_digits(123)
print(result)