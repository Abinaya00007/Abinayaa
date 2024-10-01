class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
        
class employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
        
    def display(self):
        super().display()
        print(self.salary)
        
        
a=employee("abinayaa",20,20000)
a.display()
