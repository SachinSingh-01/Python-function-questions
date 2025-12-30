'''Write a function fibonacci(n) that:
Returns the first n Fibonacci numbers as a list
Use a loop only'''
def fibonacci(n):
    fib_list=[]
    a=0
    b=1
    count=0
    while count<n:
        fib_list.append(a)
        c=a+b
        a=b
        b=c
        count+=1
    return fib_list
result=fibonacci(3)
print(result)