'''
Create a dictionary that stores each student's name and the length of the name.
Create a dictionary containing only even numbers and their squares from 1 to 20.
'''
students={'Archana','Anupama','Ansree','Ardra'}
result={name:len(name) for name in students}
print(result)

result={n:n**2 for n in range(1,21) if n%2==0}
print(result)