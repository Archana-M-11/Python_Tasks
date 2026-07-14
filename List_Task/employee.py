'''
9.Create a list contains employee data
    employee id
    name
    salary
     skills he knows(list type)
 9.1:Access data
 9.2:Add another skill
'''
#create employee data
employee = [101, "Rahul", 50000, ["Python", "Django"]]
print(employee)
#access the data
print("employee ID:", employee[0])
print("name:", employee[1])
print("salary:", employee[2])
print("skills:", employee[3])
#add another skill
skill = input("Enter new skill: ").split()
employee[3].extend(skill)
print(employee)