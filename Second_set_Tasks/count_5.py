'''
2.Count how many numbers contain the digit 5 between 1 and 1000.
'''

n=int(input('enter the first number:'))
m=int(input('enter the second number:'))
count=0
for i in range(n,m+1):
    if '5' in str(i):
        count+=1
print(count)
