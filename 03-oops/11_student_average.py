"""Practice 11: Student records and average scores.

Create a `Student` class that stores a student's name and three subject
scores. Add a method `calculate_average()` that returns the average, and a
method `show_report()` that displays the name, scores, and average. Create
two students with different scores and display both reports.
"""

class Student():
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def calculate_average(self):
        return (self.m1+self.m2+self.m3)/3

    def show_report(self):
        print(self.name, self.m1,self.m2,self.m3,self.calculate_average())

s1=Student("Abhinav",100,90,90)
s2=Student("Krishna",50,60,70)


s1.show_report()
s2.show_report()
        
