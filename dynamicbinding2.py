
class ak47:
    def defence(self):
        return "land defence"

class scar():
    def defence(self):
        return "far defence"
    
def army(protect):
    print(protect.defence())
    

a=scar()
b=ak47()
army(a)
army(b)
