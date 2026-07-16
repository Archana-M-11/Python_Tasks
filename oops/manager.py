
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
employee class il salary variable private aakku
 then Create a private method __is_valid_increment(amount),return True if the increment is greater than 0; otherwise return False.
 create an object and call method to
 Displaying employee details
Increasing the salary
Displaying the updated salary
Attempting an invalid salary increment ( example, -500) and displaying an appropriate message
 
 '''
class Employee():
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.__salary=salary
    def get_emp_id(self):
        return self.emp_id
    def get_name(self):
        return self.name
    
    def get_salary(self):     
        return self.__salary
    
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
        super().__init__(emp_id,name,salary)
        self.department=department
    def display_manager_details(self):
        print("Employee ID:", self.get_emp_id())
        print("Employee Name:", self.get_name())
        print("Department:", self.department)
        print("Salary:", self.get_salary())


manager = Manager(1001, "Rahul", 45000, "Sales")
manager.display_manager_details()
print('Annual Salary:',manager.calculate_annual_salary())
manager.increase_salary(5000)
print('Updated Salary:', manager.get_salary())
manager.increase_salary(-500)
