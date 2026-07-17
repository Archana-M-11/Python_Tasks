class Employee:

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