'''Write a function count_positive_negative(nums) that:
Returns two values:
Count of positive numbers
Count of negative numbers'''
def count_positive_negative(nums):
    count_positive=0
    count_negative=0
    for n in nums:
        if n>0:
            count_positive+=1
        else:
            count_negative+=1
    return count_positive,count_negative
listt=[3,5,-3,6,-2,-9,1]
print(count_positive_negative(listt))