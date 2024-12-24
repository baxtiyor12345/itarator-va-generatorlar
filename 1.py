# OOP itarator
class Student:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1

        if self.current < self.high:
            return self.current
        raise StopIteration
class Person:
    def __init__(self, start, stop):
        self.start = start + 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.start -= 1

        if self.start > self.stop:
            return self.start
        raise StopIteration

for elem in Student(20, -10):
   print(elem)
print(type(Student(1, 10)))
