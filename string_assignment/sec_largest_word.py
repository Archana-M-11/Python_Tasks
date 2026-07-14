'''
9.Find Second Largest Word in a sentence
'''
text=input().split()
text.sort(key=len)
ans=text[-2]
print('second largest word:',ans)
    
