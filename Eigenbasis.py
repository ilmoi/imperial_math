import numpy as np

#in numpy "matrix" - strictly 2d. need to use arrays instead.
#in numpy need to write numbers horizonally, not vertically

T = np.array([[3/2,-1],[-1/2,1/2]]) #transform
v = np.array([-1,1]) #vector to check
Ans1 = T @ T @ v

C = np.array([[2.73,1],[-1,1.366]]) #two eigenvectors 
C_inv = np.linalg.inv(C)
D = np.array([[1.866,0],[0,0.134]]) # [[eigenvalue1, 0],[0, eigenvalue2]]
new_T = C @ D @ D @ C_inv
Ans2 = new_T @ v

print('method 1 results in: ' +str(Ans1))
print('method 1 results in: ' +str(Ans2))