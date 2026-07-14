'''
3.In a tuple of student names count how many times a specific name appears.
'''
names=('Archana','Anupama','Ansree','Anagha','Aswathy','Archana')
name=input('enter the name to search:')
count=names.count(name)
print(name,'apperars',str(count),'times')