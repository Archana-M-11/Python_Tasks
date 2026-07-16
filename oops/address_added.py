class Address:
    def __init__(self, city, state, pincode):
        self.city = city
        self.state = state
        self.pincode = pincode
class Employee:
    def __init__(self, emp_id, name, salary, address):
        self.emp_id = emp_id
        self.name = name
        self.__salary = salary
        self.address = address

    def get_emp_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.__salary
    
    def employee_details(self):
        print("Employee ID:", self.get_emp_id())
        print("Employee Name:", self.get_name())
        print("Salary:", self.get_salary())
        print("City:", self.address.city)
        print("State:", self.address.state)
        print("Pincode:", self.address.pincode)
address=Address("Palakkad", "Kerala", 678001)
employee=Employee(1001, "Rahul", 45000, address)
employee.employee_details()