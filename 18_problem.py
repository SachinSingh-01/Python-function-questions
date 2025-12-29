'''Write a function calculator(a, b, operation) that:
Uses operation (+, -, *, /)
Returns the result
Handles division carefully'''
def calculator(a, b, operator):
    if (operator=="+"):
        return a+b
    elif (operator=="-"):
        return a-b
    elif (operator=="*"):
        return a*b
    if b==0:
        print("Division not possible")
    else:
        return a/b
result=calculator(3,5,"-")
print(result)