class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    
    def __lt__(self, other):
        return self.roll < other.roll
    
    def __repr__(self):
        return f"Student({self.name}, Roll={self.roll})"

students = [Student("Mahin", 12), Student("Ayesha", 5)]
print(sorted(students))  
# Output: [Student(Ayesha, Roll=5), Student(Mahin, Roll=12)]
