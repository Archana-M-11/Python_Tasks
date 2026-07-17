from .employee import Employee

class ContractEmployee(Employee):

    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        salary = hours_worked * hourly_rate
        super().__init__(emp_id, name, salary, None)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculateSalary(self):
        return self.hours_worked * self.hourly_rate