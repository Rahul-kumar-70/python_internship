"""
We have a base class Person that stores general information like name and age. We then
have multiple derived classes that represent different types of students, like
UndergraduateStudent and GraduateStudent, which both inherit from the Person class.
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)

class UndergraduateStudent(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course

    def display(self):
        super().display()
        print("course:",self.course)

class GraduateStudent(Person):
    def __init__(self,name,age,course):
        super().__init__(name,age)
        self.course=course

    def display(self):
        super().display()
        print("course:",self.course)

u=UndergraduateStudent('Rahul Kumar',25,'I.sc')
u.display()
print("----------------------------------------------------")
g=GraduateStudent('Nitish Kumar',24,'B.sc')
g.display()

