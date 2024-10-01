class vote(Exception):
    pass
def age():
    a=18
    b=int(input("enter the age"))
    try:
        if(b<a):
            raise vote
        print("he can vote")
    except vote as e:
        print("he cannot vote under age mf ")
        
age()
