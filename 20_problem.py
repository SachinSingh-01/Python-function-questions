'''Write a function word_count(sentence) that:
Returns the number of word in a sentence
Do not use len(sentence.split())'''
def word_count(sentence):
    count=0
    word=False
    for s in sentence:
        if s!=" " and not word:
            count+=1
            word=True
        elif s==" ":
            word=False
    return count
result=word_count("Hey my name is sachin aka billa")
print(f"No. of word present in sentences:{result}")