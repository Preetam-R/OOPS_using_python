# ABSTRATION 
# -> Hiding unnecesary details from users through class,methods

class Student():
    def __init__(self,name,grade,percentage):      #__init__ - refers to initialisation method or Constructor
        self.name = name
        self.grade = grade
        self.percentage = percentage
    
    def student_details(self):
        print(f'{self.name} is studying in class {self.grade}, has {self.percentage}% of attendance')

        #this above method is hidden from the user so it is called abstraction

    
    

