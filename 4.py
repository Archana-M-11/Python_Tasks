'''
Create an array of  integer elements and search an element in array.If element is found print the message element found in the position {index}
otherwise element not found
'''
arr=list(map(int,input('enter teh list : ').split()))
num=int(input('enter the number to serach : '))

if num in arr:
    print('number fount at ',arr.index(num))
else:
    print('number not found')