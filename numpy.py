import numpy as np
a=np.array([[2,2],[1,-1]])
b=np.array([1,0])
solution=np.linalg.solve(a,b)
print(solution)
