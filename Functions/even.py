'''
5.Using lambda function to return only even numbers from a list
'''
n=list(map(int, input("Enter numbers: ").split()))
even=list(filter(lambda x : x%2==0 , n))
print(even)