class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __str__(self):
        return f"The employee name is {self.name} and the age is {self.age} and the salary is {self.salary}"
    
    def __len__(self):
        return self.age
tom=Employee("Tom",47,75000)
print(tom)
print(len(tom))
#These are also called magic methods and are used for overloading a method for a specific class.
