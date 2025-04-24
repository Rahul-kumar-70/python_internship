"""
We are modeling a Student class that can inherit from two different classes:
1. Academic: This class holds academic-related information like grades and subjects.
2. Extracurricular: This class holds extracurricular-related information like activities and
awards.
The Student class will inherit from both Academic and Extracurricular, thus allowing the
student to have both academic and extracurricular information.
"""
class Academic:
    def __init__(self,grades,subjects):
        self.grades=grades
        self.subjects=subjects

class Extracurricular:
    def __init__(self,activities,awards):
        self.activities=activities
        self.awards=awards

class Student(Academic,Extracurricular):
    def __init__(self,name,grades,subjects,activities,awards):
        Academic.__init__(self,grades,subjects)
        Extracurricular.__init__(self,activities,awards)
        self.name=name
    def display(self):
        print("Name:",self.name)
        print("Grade:",self.grades)
        print("Subject:",self.subjects)
        print('Activaties:',self.activities)
        print('Awards:',self.awards)
s=Student('Rahul','A','python','Cricket',3)
s.display()