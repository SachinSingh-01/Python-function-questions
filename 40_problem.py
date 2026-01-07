'''Write a function count_upper_lower(s) that:
Returns number of uppercase and lowercase letters
Ignore digits and symbols'''
def count_upper_lower(s):
    count_upper=0
    count_lower=0
    for char in s:
        if char.isalpha():
            if char.isupper():
                count_upper+=1
            elif char.islower():
                count_lower+=1
            
    return count_upper,count_lower
result="My Name si 1243"
print(count_upper_lower(result))