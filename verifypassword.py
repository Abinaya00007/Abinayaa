class Password:
    def __init__(self,password):
        self.password=password
    def set(self):
        Epassword=input("set the password ")
        self.Epassword=Epassword 
        
    def verifypassword(self):
        
        attempt=3
        while attempt>0:
            user=input("enter the password ") 
            if(user==self.Epassword):
                print("you have access")
                return
            else:
                attempt-=1
                print(f"incorrect password ,only {attempt} left")
        print("access denied")
    
hi= Password("hi")
hi.set()
hi.verifypassword()
