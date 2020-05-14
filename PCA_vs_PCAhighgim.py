import numpy as np

n_components = 3

x = np.array([[0,2,3,4], [1, 1,5,7], [2,0,4,2]]) #NxD

x = (x-np.mean(x, axis=0))/np.std(x, axis=0) #normalize
print('')
print('normalized x, in ML format, NxD')
print(x)

#method 1
print('================== method 1 ================')
#first find eigenvectors
N,D = x.shape
S = x.T@x/N
#eigenvectors
vals,vecs = np.linalg.eig(S)
#order, select
idx = vals.argsort()[::-1]
vecs = vecs[:,idx]
vecs = vecs[:,:n_components]
print('')
print('vecs in math format, DxD')
print(vecs)
#next project x
p = vecs@vecs.T
ans = x@p
print('')
print('answer is')
print(ans)

#method 2
print('================== method 2 ================')
XX = x@x.T #NxN
#eigenvectors
vals,vecs = np.linalg.eig(XX)
vecs = x.T@vecs
vecs = vecs/np.linalg.norm(vecs,axis=0) #note how direction (minuses or pluses) don't matter - there can be opposite eigenvectors for the same eigenvalue
#order, select
idx = vals.argsort()[::-1]
vecs = vecs[:,idx]
vecs = vecs[:,:n_components]
print('')
print('vecs in math format, DxD')
print(vecs)
#next project x
p = vecs@vecs.T
ans = x@p
print('')
print('answer is')
print(ans)
