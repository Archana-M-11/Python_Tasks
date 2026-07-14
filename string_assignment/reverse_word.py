'''
5.Take a sentence from user and reverse words
Input : "Python is powerful"
     Output : "powerful is Python"
'''
text=input('Enter the string : ')
for ch in text:
    text=text[::-1]
print(text)