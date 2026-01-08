'''Write a function find_missing_number(nums) that:
List contains numbers from 1 to n
One number is missing
Return the missing number'''
def find_missing_number(nums):
    sums=0
    for n in nums:
        sums+=n
    total = (len(nums) + 1) * (len(nums) + 2) // 2
    return total-sums
result=[1,2,4,5]
print(find_missing_number(result))