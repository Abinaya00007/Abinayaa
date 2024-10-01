class abinaya:
    def __init__(self):
       pass
    
    def __iter__(self):
        self.num=1
        return self
    
    def __next__(self):
        if self.num<=10:
            value=self.num
            self.num+=1
            return value
        else:
             raise StopIteration
        
a=abinaya()
for value in a:
    print(value)
