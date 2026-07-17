from .employee import Employee

class PermanentEmployee(Employee):

    def __init__(self, emp_id, name, salary, department, bonus):
        super().__init__(emp_id, name, salary, department)
        self.bonus = bonus

    def calculateSalary(self):
        return self.get_salary() + self.bonus