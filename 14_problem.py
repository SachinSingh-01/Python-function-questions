'''Write a function sum_and_product(a, b) that:
Returns both sum and product of two numbers
Print both values after calling the function'''
def sum_and_product(a,b):
    return a+b,a*b
sum_result,product_result=sum_and_product(4,6)
print(f"Sum of two number:{sum_result}")
print(f"Product of two number:{product_result}")
