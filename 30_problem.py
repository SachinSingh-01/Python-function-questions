'''Write a function merge_lists(list1, list2) that:
Merges two lists
Returns a single list without using + operator'''
def merge_list(list1, list2):
    list1.extend(list2)
    return list1
result=merge_list(list1=[2,3,4,6,1],list2=[4,7,9,2])
print(result)
