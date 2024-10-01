def prime(num):
 for i in range(2,abi+1):
    if(abi%i!=0):
        return True
    else:
        return False
abi=int(input("enter the number"))
print(prime(abi))
