from .employee import Employee


class Manager(Employee):

    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary, department)

    def display_manager_details(self):
        print("Employee Details")
        print("Employee ID:", self.get_emp_id())
        print("Employee Name:", self.get_name())
        print("Department ID:", self.get_department().get_dept_id())
        print("Department Name:", self.get_department().get_dept_name())
        print("Salary:", self.get_salary())

    def calculate_annual_salary(self):
        return self.get_salary() * 14
    
