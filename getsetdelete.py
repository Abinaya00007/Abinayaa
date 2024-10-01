
class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def set(self):
        name=input("enter the name")
        color=input("enter the color")
        self.name=name
        self.color=color 
        
    def get(self):
        print(self.name,self.color) 
        
    def delete(self):
       del self.name
        
car=Car("abinaya","red")
car.get()

car.set()
car.get()

car.delete()
print(car.__dict__)
