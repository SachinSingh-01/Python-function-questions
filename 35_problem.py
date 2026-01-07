'''Write a function capitalize_words(sentence) that:
Capitalizes the first letter of each word
Returns the updated sentence
Do not use title().'''
def capitalize_word(sentence):
    words = sentence.split()
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:])
    return " ".join(result)
text=("My name sachin")
print(capitalize_word(text))
