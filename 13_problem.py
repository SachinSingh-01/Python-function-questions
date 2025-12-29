'''Write a function count_even(nums) that:
Takes a list of numbers
Returns how many even numbers are in the list'''
def count_even(nums):
    count=0
    for i in nums:
        if i%2==0:
            count+=1
    return count
nums=[3,5,6,2,8,9,2]
result=count_even(nums)
print("No. of even numbers:",result)