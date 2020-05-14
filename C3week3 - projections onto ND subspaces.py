

import numpy as np
x = np.array([12,0,0])
B = np.array([[1,0],[1,1],[1,2]])

print('x is: ' +str(x))
print('B is: ' +str(B))

print('-')
print('BTx is: ' +str(B.T@x))
print('BTB is: ' +str(B.T@B))

print('-')
p = B@np.linalg.inv(B.T@B)@B.T
print('projection matrix is: ' +str(p))
print('actual vector is: ' +str(p@x))

x = np.linalg.inv(B.T@B)