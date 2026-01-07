'''Write a function split_even_odd(nums) that:
Returns two lists:
One with even numbers
One with odd numbers'''
def split_even_odd(nums):
    even_list=[]
    odd_list=[]
    for n in nums:
        if n%2==0:
            even_list.append(n)
        else:
            odd_list.append(n)
    return even_list,odd_list
lst=[2,3,4,7,9,1,3]
print(split_even_odd(lst))