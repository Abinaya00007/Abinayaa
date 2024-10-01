class student:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        
    def increase(self,amount):
        self.salary+=amount
        print(self.salary)
        
    def display(self):
        print(self.name)
        print(self.age)
        
# mark=[30,40,50,60,90]
stu=student("abinaya","15",20000)
stu.display()
print("before salary increament")
stu.increase(0)
print("after salary increament")

stu.increase(20000)
