"""Practice 7: Instance methods and self.

Create a `Counter` class. Its constructor should start the count at zero.
Add an `increment` method that increases this object's count by one and a
`show_count` method that displays it. Create two counters and increment one
of them twice. Show both counts to confirm each object has its own state.
"""

class Counter:
    def __init__(self):
        self.count=0

    def increment(self):
        self.count += 1

    def show_count(self):
        print(self.count)

c1= Counter()
c2= Counter()
c1.increment()
c1.increment()
c1.show_count()
c2.show_count()
