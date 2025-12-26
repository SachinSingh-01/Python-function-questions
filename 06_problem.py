'''Write a function add_default(a, b=10) that returns the sum of a and b.
Call the function:
Once with one argument
Once with two arguments'''
def add_default(a,b=10):
    return a+b
total=add_default(4)
total2=add_default(7,10)
print(f"Once with a:{total}")
print(f"Once with a and b:{total2}")
# add_default(4)
# add_default(4,10)