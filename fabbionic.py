def fabo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fabo(n-1)+fabo(n-2))
n=int(input("enter the number"))    
for i in range(n):
   print(fabo(i),end="  ")
