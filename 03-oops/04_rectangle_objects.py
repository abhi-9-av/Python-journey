"""Practice 4: Give each object its own attributes.

Create a `Rectangle` class whose constructor receives width and height. Add an
`area` method that returns width multiplied by height. Create two rectangles
with different dimensions and print each area.
"""

class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.height * self.width

rec1 = Rectangle(10,20)
rec2 = Rectangle(20,30)

print(rec1.area())
print(rec2.area())


