# Instance variables belong to one object; class variables are shared by all objects.
class Employee:
    company = "Tech Labs"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Aditi", 30000)
emp2 = Employee("John", 35000)

print(emp1.name, emp1.salary, emp1.company)
print(emp2.name, emp2.salary, emp2.company)
