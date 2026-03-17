# INHERITANCE
# -> allows one class(child) to use the property and method of another class(parent)

class Student():
    def __init__(self,name,grade,percentage):      #__init__ - refers to initialisation method or Constructor
        self.name = name
        self.grade = grade
        self.percentage = percentage
    
    def student_details(self):
        print(f'{self.name} is studying in class {self.grade}, has {self.percentage}% of attendance')

# now lets make child class 
class Graduate(Student):
    def __init__(self,name,grade,percentage,stream): #parametrer passed from parent class and in new child class
        super().__init__(name,grade,percentage) #calling parent class 
        self.stream = stream  #New attribute in child class

    def deatils(self):
        if self.percentage > 35:
            print(f'{self.name} has cleared {self.grade} {self.stream} and has secured {self.percentage}')
        else:
            print(f'{self.name} has failed {self.grade} {self.stream} and has secured {self.percentage}')
    

student1 = Graduate('Preetam',12,95,"Science")
student2 = Graduate('Sammy',12,30,"Science")

student1.deatils()
student2.deatils()


