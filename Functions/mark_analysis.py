'''
Create a function result_analysis(*marks, **student)
 
Display:
 
Student Name
Highest Mark
Lowest Mark
Average
Grade using the following rules:
Average ≥ 90 → A+
Average ≥ 80 → A
Average ≥ 70 → B
Average ≥ 60 → C
Otherwise → Fail
'''
def result_analysis(*marks,**student):
    avg=sum(marks)/len(marks)
    highest=max(marks)
    lowest=min(marks)
    if avg>=90:
        grade='A+'
    elif avg>=80:
        grade='A'
    elif avg>=70:
        grade='B'
    elif avg>=60:
        grade='C'
    else:
        grade='FAIL'
    print('Student Name:',student['name'])
    print('highest mark:',highest)
    print('lowest mark:',lowest)
    print('average mark:',avg)
    print('grade:',grade)        
result_analysis(
    85, 92, 78, 88, 95,
    name="Archana"
)