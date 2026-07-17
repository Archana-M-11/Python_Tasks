'''
Create a class named Department.
Define a constructor (__init__) that initializes:
dept_id
dept_name
Create getter methods:
get_dept_id()
get_dept_name()
Modify the Employee class so that it has a Department object.
Add a parameter named department to the constructor.
Store the Department object as an instance variable.
Create a getter method:
get_department()
While displaying employee details, display:
Department ID
Department Name
Create a Department object with the following details:
Department ID: D101
Department Name: Sales
Create a Manager object by passing the Department object to the constructor.
Display:
Employee Details
Department Details
Annual Salary
Increase the salary by 5000 and display the updated salary.
'''
class Department():
    def __init__(self,dept_id,dept_name):
        self.dept_id=dept_id
        self.dept_name=dept_name
    def get_dept_id(self):
        return self.dept_id
    def get_dept_name(self):
        return self.dept_name
     

class Employee():
    def __init__(self,emp_id,name,salary,department):
        self.emp_id=emp_id
        self.name=name
        self.__salary=salary
        self.department=department
    def get_emp_id(self):
        return self.emp_id
    def get_name(self):
        return self.name
    
    def get_salary(self):     
        return self.__salary
    
    def get_department(self):
        return self.department
    
    def __is_valid_increment(self, amount):
        return amount > 0
    def increase_salary(self, amount):
        if self.__is_valid_increment(amount):
            self.__salary += amount
            print(f"Salary increased by: {amount}")
            print("Salary Updated Successfully")
        else:
            print("Invalid Increment Amount")
    def calculate_annual_salary(self):
        return self.__salary * 12
    
class Manager(Employee):
    def __init__(self,emp_id, name, salary, department):
        super().__init__(emp_id,name,salary,department)
    def display_manager_details(self):
        print("Employee ID:", self.get_emp_id())
        print("Employee Name:", self.get_name())
        print("Department ID:", self.get_department().get_dept_id())
        print("Department Name:", self.get_department().get_dept_name())
        print("Salary:", self.get_salary())
    def calculate_annual_salary(self):
        return self.get_salary() * 14
    
department=Department('D101','Sales')
manager = Manager(1001, "Rahul", 45000, department)
print('Employee Details')
manager.display_manager_details()
print('Annual Salary:', manager.calculate_annual_salary())
manager.increase_salary(5000)
print('Updated Salary:', manager.get_salary())