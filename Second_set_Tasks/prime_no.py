'''
1.Print all prime numbers between 100 and 200
'''
n=int(input('first number: '))
m=int(input('second number: '))
ans=[]
for num in range(n, m + 1):
    prime = True
    if num < 2:
        prime = False
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        ans.append(num)
print("Prime numbers:", ans)
        


