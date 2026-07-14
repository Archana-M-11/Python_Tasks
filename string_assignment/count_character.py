'''2. Count how many times "s" appears in "Mississippi"'''
word='Mississippi'
count=0
count=word.lower().count('s')
for ch in word:
    if ch=='s' or 'S':
        count+=1
print('s occured for',count,'times')
    
