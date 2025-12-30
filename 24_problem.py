'''Write a function second_largest(nums) that:
Takes a list of numbers
Returns the second largest number
Do not use sort() or max().'''
def second_largest(nums):
    if len(nums) < 2:
        return None
    largest = None
    second = None
    for num in nums:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    return second
print(second_largest([3, 4, 2, 6, 7]))
