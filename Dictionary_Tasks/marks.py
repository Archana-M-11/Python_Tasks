'''
3.Store marks of five subjects in a dictionary.
Calculate:
Total marks.
Average.
Highest mark.
Lowest mark.
 '''
Marks={
     "Maths": 90,
    "Science": 85,
    "English": 88,
    "Python": 95,
    "Social": 80
}
total=sum(Marks.values())
average=sum(Marks.values())/len(Marks)
highest=max(Marks.values())
lowest=min(Marks.values())
print('Total Marks: ',total)
print('average Marks: ',average)
print('highest Marks: ',highest)
print('lowest Marks: ',lowest)