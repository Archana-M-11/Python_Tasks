'''
2.Create a set of unique vowels from the string "programming".
'''
word='programming'
vowels={ch for ch in word if ch in 'aeiouAEIOU'}
print(vowels)