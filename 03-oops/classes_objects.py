# A class defines a blueprint, and an object is an instance of that class.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def intro(self):
        return f"{self.name} has grade {self.grade}."

student = Student("Rahul", "A")
print(student.intro())
