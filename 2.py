'''
2.Calculate sum of all odd numbers from 1 to 50?
'''
n = int(input("tarting number: "))
m = int(input("Eending number: "))
sum = 0
for i in range(n, m + 1):
    if i % 2 != 0:
        sum += i
print("Sum =", sum)
