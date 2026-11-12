"""Practice 6: Class attributes, instance attributes, and precedence.

Create an `Employee` class with a class attribute `company = "Northstar"`.
Each employee should have their own name and salary. Create two employees
and display their details. Then set `company` on only the first employee to
"Bright Labs" and display both again. Observe which value each object uses.
"""

class Employee:
    company="Northstar"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
   

Emp1 = Employee("Abhinav",100000)
Emp2 = Employee("Krishna",50000)


print(Emp1.name,Emp1.salary,Emp1.company)
print(Emp2.name,Emp2.salary,Emp2.company)
Emp2.company="Bright Labs"
print(Emp2.name,Emp2.salary,Emp2.company)
