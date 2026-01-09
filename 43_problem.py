'''Write a function longest_word(sentence) that:
Takes a sentence
Returns the longest word
If multiple words have the same length, return the first one.'''
def longest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word("Hi my name is Billa from pluto"))