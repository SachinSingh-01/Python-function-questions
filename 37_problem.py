'''Write a function remove_vowels(s) that:
Removes all vowels from a string
Returns the new string'''
def remove_vowels(s):
    result=""
    vowel='aeiouAEIOU'
    for char in s:
        if char not in vowel:
            result+=char
    return result
print(remove_vowels("hey my name is billa"))
                