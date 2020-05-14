import numpy as np

T = np.array([[3/2,-1],[-1/2,1/2]]) #transform
vals, vecs = np.linalg.eig(T)
C = vecs

#C = np.array([[-2.73,0.73],[1,1]]) #two eigenvectors form together eigen transform
C_inv = np.linalg.inv(C)
D = C_inv @ T @ C #not siply taking diagonal and filling 0s!!!! need to calculate using this equation: D=C−1TC.
print(D)