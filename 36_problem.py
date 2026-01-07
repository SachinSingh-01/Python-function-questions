'''Write a function common_elements(list1, list2) that:
Returns a list of common elements
No duplicates in the result'''
def common_elements(list1, list2):
    result=[]
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result
list1=[1,2,4,4,2,1]
list2=[3,5,8,1,2,5]
print(common_elements(list1,list2))