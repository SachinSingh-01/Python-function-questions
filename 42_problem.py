'''Write a function is_anagram(s1, s2) that:
Returns True if both strings are anagrams
Ignore case and spaces'''
def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    if len(s1) != len(s2):
        return False
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
    for value in count.values():
        if value != 0:
            return False
    return True
print(is_anagram("Listen", "Silent"))       
print(is_anagram("Dormitory", "Dirty room"))
print(is_anagram("moni", "sachin"))         
