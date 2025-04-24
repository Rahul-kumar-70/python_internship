"""
We have a system where we want to model different aspects of a Student. A Student has
both Academic and Extracurricular attributes. At the same time, we have two types of
students: UndergraduateStudent and GraduateStudent, each requiring specific information
related to their academic status. Therefore, we can use Hybrid Inheritance, which combines
Multiple Inheritance (for combining Academic and Extracurricular features) and
Hierarchical Inheritance (for having different types of students like UndergraduateStudent
and GraduateStudent).
"""

class Academic:
    def __init__(self,grades,subjects):
        self.grades = grades
        self.subjects = subjects
class Extracurricular:
    def __init__(self,activities,awards):
        self.activities = activities
        self.awards = awards
class student(Academic,Extracurricular):
    def __init__(self,name,age,grades,subjects,activities,awards):
        Academic.__init__(self,grades,subjects)
        Extracurricular.__init__(self,activities,awards)
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Grades:",self.grades)
        print("Subjects:", self.subjects)
        print("Activities:", self.activities)
        print("Awards:", self.awards)

class UndergraduateStudent(student):
    def __init__(self,name,age,grades,subjects,activities,awards,course):
        super().__init__(name,age,grades,subjects,activities,awards)
        self.course=course

    def display(self):
        super().display()
        print("Course:",self.course)

class GraduateStudent(student):
    def __init__(self,name,age,grades,subjects,activities,awards,course):
        super().__init__(name,age,grades,subjects,activities,awards)
        self.course=course

    def display(self):
        super().display()
        print("course:",self.course)

u=UndergraduateStudent('Rahul Kumar',24,'A','Python','cricket',2,'I.Sc')
u.display()
print("------------------------------------------------")
g=GraduateStudent('vimlesh Kumar',24,'A','Java','cricket',2,'B.sc')
g.display()