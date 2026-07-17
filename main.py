from oops_package.department import Department
from oops_package.manager import Manager
from oops_package.project import Project


project = Project("P101", "Banking System")

department = Department("D101", "Sales")
manager = Manager(1001, "Rahul", 45000, department)
manager.display_manager_details()
print(manager)

manager.workOnProject(project)

print('Annual Salary:',manager.calculate_annual_salary())
manager.increase_salary(5000)
print('Updated Salary:', manager.get_salary())
manager.increase_salary(-500)
print('Bonus: ',manager.calculate_bonus())
manager2 = Manager(1003, "Anu", 60000, department)
print('manager == manager2: ',manager == manager2)
print('manager < manager2: ',manager < manager2)

