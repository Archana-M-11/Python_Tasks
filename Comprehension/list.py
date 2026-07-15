'''
Create a list of the lengths of each word in a sentence
'''
sentence = "Python is easy"
lengths = [len(word) for word in sentence.split()]
print(lengths)