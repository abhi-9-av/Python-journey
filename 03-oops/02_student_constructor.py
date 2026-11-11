"""Practice 2: Initialize an object with a constructor.

Create a `Student` class. Its constructor should receive a name and grade and
save them as attributes. Create two students and print each student's details.
"""

class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade


s1 =Student(input("Enter the name"),input("Enter the grades"))
s2 =Student(input("Enter the name"),input("Enter the grades"))
print(s1.name,s1.grade)
print(s2.name,s2.grade)