class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, lang):
        super().__init__(name, salary)  # Inherit from Employee
        self.lang = lang

# Usage
dev = Developer("Alice", 80000, "Python")
print(f"{dev.name} codes in {dev.lang}")
