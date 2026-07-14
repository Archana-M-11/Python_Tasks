'''
8. Character Frequency Counter

    Input : "Programming"

Output :p : 1 ,r : 2,o : 1 etc.


'''
text=input()
dict={}
for ch in text:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
for key,value in dict.items():
     print(key, ":", value)
