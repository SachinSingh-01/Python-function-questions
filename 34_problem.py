'''Write a function count_digits(n) that:
Takes an integer
Returns the number of digits'''
def count_digits(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
result=count_digits(123335)
print("No. of digit present:",result)