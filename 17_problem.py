'''Write a function find_min(*nums) that:
Accepts variable-length arguments
Returns the smallest number
Do not use min().'''
def find_min(*nums):
    smallest=nums[0]
    for i in nums:
        if i<smallest:
            smallest=i
    return smallest
result=find_min(3,4,2,7,1,7)
print(f"Smallest number:{result}")