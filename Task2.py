class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, studying {self.course}.")

student1 = Student("Joefil P. Villaruel", 29, "DIP-IT")
student2 = Student("laarni", 22, "Engineering")
student3 = Student("mealone", 21, "Mathematics")

student1.introduce()
student2.introduce()
student3.introduce()
