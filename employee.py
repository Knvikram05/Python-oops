class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        print(self.name, self.salary, self.department)

m = Manager("Vikram", 50000, "Dev")
m.display_details()