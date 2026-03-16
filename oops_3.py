#modifying the object property

class Student():
    def __init__(self,name,grade,percentage):      #__init__ - refers to initialisation method or Constructor
        self.name = name
        self.grade = grade
        self.percentage = percentage
    
    def student_details(self):
        print(f'{self.name} is studying in class {self.grade}, has {self.percentage}% of attendance')

# lets create one object


student1 = Student("Preetam", 12, 98)
student1.student_details()

#  modify the percentage the value of percentage attribute 
student1.percentage = 99
student1.student_details()  # so we can modify object property

# delete object Property 
# del student1.percentage


#delete entire object 
# del student1


