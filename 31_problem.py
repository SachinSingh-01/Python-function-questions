'''Write a function char_frequency(s) that:
Returns a dictionary of character frequencies
Ignore spaces'''
def char_frequency(s):
    dic={}
    for char in s:
        if char!=" ":
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
    return dic
result=char_frequency("appleapp")
print(result)