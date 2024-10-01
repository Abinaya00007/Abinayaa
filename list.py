items=['marker','oen',1,2,2.3]
number=[]
string=[]
for i in items:
  
    if isinstance(i, (int)):
        number.append(i)

    else :
        string.append(i)
    
print(string)
print(number)
