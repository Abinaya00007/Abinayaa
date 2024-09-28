class horin:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return(self.x-other.x,self.y-other.y)
p=horin(1,2)
q=horin(6,7)
x=p+q
e=p-q

print(x)
print(e)


import datetime
print(datetime.now(timezone.utc))
