#encapsulation
# -> Restrict access to certain attributes or methods to protect the data and enforced controlled access


class Student():
    def __init__(self,name,grade,percentage):      #__init__ - refers to initialisation method or Constructor
        self.name = name
        self.grade = grade
        self.__percentage = percentage # double unsderscore limits the access

    def get_percentage(self):   #using "get" is best practice to write method for encapsulation
        return self.__percentage

    def student_details(self):
        print(f'{self.name} is studying in class {self.grade}, has {self.percentage}% of attendance')

student1 = Student("Preetam",12,99)
# print(student1.__percentage)  # this will give error bcz we have restricted the access 

print(student1.get_percentage())