print("abinaya")
list=[1,2,3]
print(list)
list.append(1)
print(list)
list.pop()
print(list)
str1="abinaya daju ra daju"
str2="     WORLD"
result=str1+str2
print(result)
first_name=result[:5]
print(first_name)
print(str1.upper())
print(str2.lower())
print(str2.strip(" "))
print(str1.replace("abinaya daju","abishek daju"))
print(f"my name is {str1,str2 }")
print(len(str1+str2))
print("letter word",len(str1),"is good")
a="harry"
print(a[-4:-2]) 
print(str1.capitalize()) #first letter capital ma lagxa aaani aaru small ma lagxa 
print(str1.count("daju"))
print(str1.endswith("")) #ending ma ke xa herxa 
print(str1.find("ra"))   
print(str1.index("ra"))   #yedi word xaina vane siddhai out hunxa program
print(str1.isupper()) #capital xa ki xaina herxa
print(str1.islower()) #small xa ki xaina herxa
print(str1.isprintable()) #printable xa ki xaina herxa \n hudaina 
print(str1.isspace()) #white space xa ki xaina herxa
print(str2.swapcase()) #upper vaye lowwer lower vaye upper
for i in str1:
  print(i)
  if (i=="d"):
    print("this is something special") 
for i in range(0,2):
  print(f"{str1}")
  i=0
  while(i<3):
   print(i)
   i=i+1
for i in range(0,10+1):
  print("5 X",i,"=",5*(i+1))
