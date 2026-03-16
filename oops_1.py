#  OOPS 

# We all know that oops contains class and objects
# Class contains methods and attributes

# lets create the students record using oops

# creating the class

class Student():
    def __init__(self,name,grade):      #__init__ - refers to initialisation method or Constructor
        self.name = name
        self.grade = grade


#lets create the object for class Student

stud_1 = Student('Preetam',12)
print(stud_1.name,stud_1.grade)
print(f'{stud_1.name} studying in class {stud_1.grade}')

#now i can use Multiple value for storing the records

stud_2 = Student('Roy',10)
print(f'\n{stud_2.name} studying in class {stud_2.grade}')

