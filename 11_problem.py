'''Write a function find_max(a, b, c) that:
Takes three numbers
Returns the largest number
Do not use max().'''
def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
result=find_max(12,45,2)
print(result)