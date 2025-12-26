'''Write a function total_sum(*nums) that accepts multiple numbers and prints their sum.
Example call:total_sum(1, 2, 3, 4)'''
def total_sum(*n):
    add=0 
    for i in n:
        add+=i
    print(f"Addition of multiple number:{add}")
total_sum(1,2,3,4)