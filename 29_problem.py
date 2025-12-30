# write a python program using function to print fibonacci series up to n terms.
def fibonacci(n):
    a=0
    b=1
    count=0
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
    return
fibonacci(3)
