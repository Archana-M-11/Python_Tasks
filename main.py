from oops_package.department import Department
from oops_package.project import Project
from oops_package.manager import Manager
from oops_package.permenantEmployee import PermanentEmployee
from oops_package.contractEmployee import ContractEmployee



department = Department("D101", "Sales")
project = Project("P101", "Banking System")



manager = Manager(1001, "Rahul", 45000, department)
print(manager)

manager.workOnProject(project)
print("Annual Salary:", manager.calculate_annual_salary())

manager.increase_salary(5000)
print("Updated Salary:", manager.get_salary())

manager.increase_salary(-500)

print("Bonus:", manager.calculate_bonus())
print("Manager Salary (Basic + Bonus):", manager.calculateSalary())
manager2 = Manager(1003, "Anu", 60000, department)
print("manager == manager2 :", manager == manager2)
print("manager < manager2  :", manager < manager2)
permanent = PermanentEmployee(101,"Ramesh",50000,department,10000)
print("PERMANENT EMPLOYEE")
print("Salary:", permanent.calculateSalary())
contract = ContractEmployee( 102,"Anu",120,300)
print("CONTRACT EMPLOYEE")
print("Salary:", contract.calculateSalary())