'''Write a function char_count(sentence) that:
Returns the number of character in a sentence
Do not use len(sentence.split())'''
def char_count(sentence):
    count=0
    for s in sentence:
        if sentence:
            count+=1
    return count
result=char_count("My name is sachin singh learning python")
print(f"No. of words present in sentences{result}")
