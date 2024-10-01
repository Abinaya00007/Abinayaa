class love(Exception):
    def __init__(self,message="you can't love"):
     super().__init__(message)
     
age=int(input("enter the age "))
try:
    if age<18:
        raise love()
    print("he can love")
    
except Exception as e:
    print(e)
