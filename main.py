from oops_package.department import Department
from oops_package.manager import Manager

department = Department("D101", "Sales")
manager = Manager(1001, "Rahul", 45000, department)
manager.display_manager_details()
print('Annual Salary:',manager.calculate_annual_salary())
manager.increase_salary(5000)
print('Updated Salary:', manager.get_salary())
manager.increase_salary(-500)
