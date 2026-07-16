'''Create a class named Employee.
Define a constructor (__init__) that initializes the following attributes:
emp_id
name
salary
Create the following getter methods:
get_emp_id()
get_name()
get_salary()
Create an Employee object with the following details:
Employee ID: 1001
Name: Rahul
Salary: 45000
Use the getter methods to display the employee details
add method calculate_anual_salary() that returns the employee's annual salary.
 '''
class Employee():
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def get_emp_id(self):
        return self.emp_id
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def calculate_anual_salary(self):
        return self.salary*12
employee = Employee(1001, "Rahul", 45000)
print('EmployeeID: ',employee.get_emp_id())
print('Employee Name: ',employee.get_name())
print('Employee Salary: ',employee.get_salary())
print('Employee Annual Salary: ',employee.calculate_anual_salary())