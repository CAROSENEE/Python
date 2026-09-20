class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"Student({self.name!r}, {self.age})"


s1 = Student("Mahin", 22)

print(s1)         # __str__ call hoy
print(repr(s1))   # __repr__ call hoy
print([s1])       # list er vitore __repr__ dekhay