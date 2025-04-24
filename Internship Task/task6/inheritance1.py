"""
We want to model a system where we have a base class for Person that contains basic
information (like name and age). Then, we have a Student class that inherits from Person
and adds information about the student's roll_number and grades. Finally, we have a
GraduateStudent class that inherits from Student and adds additional attributes like the
degree they are pursuing.
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,roll_number,grades):
        super().__init__(name,age)
        self.roll_number=roll_number
        self.grades=grades
class GraduateStudent(Student):
    def __init__(self,name,age,roll_number,grades,degree):
        super().__init__(name,age,roll_number,grades)
        self.degree=degree
    def display(self):
        print('Name:',self.name)
        print('Age:', self.age)
        print('Roll No:', self.roll_number)
        print('Grades:', self.grades)
        print('Degree:', self.degree)

g=GraduateStudent('Rahul kumar',25,10,'A','M.C.A')
g.display()