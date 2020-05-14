import numpy as np

#I have 3 examples with 2 dimensions each
x = np.array([[0, 2], [1, 1], [2, 0]]) #N by D = 3 by 2

#subtracting mean
x = x-np.mean(x,axis=0)

#using numpy's built in function, requires us to transpose the matrix because numpy wants to see examples as rows
#turns out numpy is dividing by N-1, not N
method1 = np.cov(x.T)
print('method1')
print(method1)

#manual method from the lecture. note this only works because we subtracted mean before (normalized)
method2 = x.T@x/(x.shape[0]-1)
vals,vecs = np.linalg.eig(method2)
print('method2')
print(method2)