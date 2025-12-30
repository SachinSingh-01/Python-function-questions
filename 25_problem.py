'''Write a function remove_duplicates(nums) that:
Takes a list
Returns a new list with duplicates removed
Maintain original order'''
def remove_duplicates(nums):
    duplicate=set(nums)
    return duplicate
result=remove_duplicates([2,4,5,6,2,4,5])
print(list(result))

