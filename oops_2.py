# now lets see how to implement other methods and features of class

#lets consider previous class (Student)

class Student():
    def __init__(self,name,grade):      #__init__ - refers to initialisation method or Constructor
        self.name = name
        self.grade = grade
    
    def student_details(self):
        print(f'{self.name} is studying in class {self.grade}')

#creating the object

stud_1 = Student('Preetam',12)
stud_2 = Student("Carlos",11)

stud_1.student_details()
stud_2.student_details()

print(stud_1.__dict__)   #this gives output in form of dictionary
