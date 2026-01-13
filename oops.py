class Student:
    college = "Parul University"   # class variable

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    
    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

std_1 = Student('Raghav', 13, 90)
std_2 = Student('Vishal', 17, 97)

print(std_1.college)