matrix1=[[1,2,3],
         [4,5,6],
         [7,8,9]
         ]
matrix2=[[9,10,11],
         [4,5,6],
         [7,8,9]
         ]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]
        ]

result2=[[0,0,0],
        [0,0,0],
        [0,0,0]
        ]

result3=[[0,0,0],
        [0,0,0],
        [0,0,0]
        ]

for i in range (len(matrix1)):
    for j in range (len(matrix1[0])):
        
        result[i][j]=matrix1[i][j]+matrix2[i][j]
        result2[i][j]=matrix1[i][j]-matrix2[i][j]
        result3[j][i]=matrix1[i][j] #transpose


for i in result:  #yo layena vane [],[],[] yesari value aauxa 
  print(i)        
  
for i in result2: 
   print(i)
  
for i in  result3:
  print(i)
