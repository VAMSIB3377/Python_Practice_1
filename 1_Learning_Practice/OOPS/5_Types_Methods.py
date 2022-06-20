# 1. Instance Methods --> Accessor Methods -> Used To Fetch The Values
#                     --> Mutator Methods  -> Used to Modify the Values
# 2. Class Methods
# 3. Static Methods


class Student:
    school = "ABCD"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # Instance Method
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):  # Class Method
        return cls.school

    @staticmethod
    def info():  # Static Method
        return "This is Student Class.. In xyz Module"


s1 = Student(10, 20, 30)
s2 = Student(90, 80, 70)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())

print(Student.info())
