'''
2.Store marks of a student in a tuple and slice the tuple to print
    2.1.first three scores
    2.2.last two scores
    2.3.Middle scores
'''
marks=(85,90,98,70,60,80)
print('first three marks:',marks[:3])
print("Last two scores:", marks[-2:])

mid = len(marks) // 2
if len(marks) % 2 == 0:
    print("Middle scores:", marks[mid-1:mid+1])
else:
    print("Middle score:", marks[mid])