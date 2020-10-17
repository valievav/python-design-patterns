import copy


class Address:
    def __init__(self, street, suite, city):
        self.street = street
        self.suite = suite
        self.city = city

    def __str__(self):
        return f"{self.street}, suite #{self.suite}, {self.city}."


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} works at {self.address}"


# factory to generate different TYPES of employee
# stateless - does operations through static methods
class EmployeeFactory:
    main_office_employee = Employee('', Address('123 Main Road', 0, 'Green City'))  # prototype
    auxiliary_office_employee = Employee('', Address('123 Secondary Road', 0, 'Green City'))  # prototype

    @staticmethod
    def __new_employee(prototype, name, suite):
        employee = copy.deepcopy(prototype)  # prototype deepcopy
        employee.name = name
        employee.address.suite = suite
        return employee

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)

    @staticmethod
    def new_auxiliary_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.auxiliary_office_employee, name, suite)


emp1 = EmployeeFactory.new_main_office_employee("Jane", 25)
emp2 = EmployeeFactory.new_main_office_employee("Corey", 1)

emp3 = EmployeeFactory.new_auxiliary_office_employee("Dany", 123)
emp4 = EmployeeFactory.new_auxiliary_office_employee("Lana", 16)
print(emp1)
print(emp2)
print('---')
print(emp3)
print(emp4)
