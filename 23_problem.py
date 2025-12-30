'''Write a function count_vowels(s) that:
Takes a string
Returns the number of vowels (a, e, i, o, u)
Case insensitive'''
def count_vowels(s):
    vowel_count=0
    for i in s:
        if i in ('a','e','i','o','u') :
            vowel_count+=1
    return vowel_count
result=count_vowels("Hey my name is sachin")
print("No. of vowel present:",result)