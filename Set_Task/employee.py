'''
2.Create a set of employee ids
Add employee ID 104.
Update the set with {105,106}.
Remove employee ID 102.
Discard employee ID 110.
Display the final set.
 
Check whether "119" exists. If not, add it.
 
'''
employee_ids = {101, 102, 103,110}

employee_ids.add(104)
employee_ids.update({105,106})
employee_ids.remove(102)
employee_ids.discard(110)
print('final Set:')
print(employee_ids)
if 119 not in employee_ids:
    employee_ids.add(119)

print('after checking 119:',employee_ids)



