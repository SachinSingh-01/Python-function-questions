'''Write a function reverse_string(s) that:
Returns the reversed string
Do not use slicing ([::-1])'''
def reverse_string(s):
    rev_string=""
    for ch in s:
        rev_string=ch+rev_string
    return rev_string
print(reverse_string("Python"))
            