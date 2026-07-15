def vowels(text):
    count=0
    vowels='aeiouAEIOU'
    for ch in text:
        if ch in vowels:
            count+=1
    return count
text=input('enter the word: ')
print(vowels(text)) 