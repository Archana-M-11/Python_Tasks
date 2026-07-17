from abc import ABC, abstractmethod
class Employee(ABC):
    
    def __str__(self):
        return (
            f"Employee ID: {self.emp_id}\n"
            f"Employee Name: {self.name}\n"
            f"Department ID: {self.department.get_dept_id()}\n"
            f"Department Name: {self.department.get_dept_name()}\n"
            f"Salary: {self.__salary}"
        )
    def __eq__(self,other):
        return self.emp_id==other.emp_id
    def __lt__(self, other):
        return self.get_salary() < other.get_salary()
    def __gt__(self, other):
        return self.get_salary() > other.get_salary()

    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.__salary = salary
        self.department = department

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
    
    def workOnProject(self, project):
        print(f"{self.get_name()} is working on:")
        project.displayProjectDetails()
    
    @abstractmethod
    def calculateSalary(self):
        pass