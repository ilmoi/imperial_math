import numpy as np

a = np.array([[-1,2,2],[2,2,-1],[2,-1,2]])
vals,vecs= np.linalg.eig(a)
#print(vals)
#print(vecs)

idx = vals.argsort()[::-1]
vals = vals[idx]
vecs = vecs[:,idx]
vecs = vecs.T

print(vals)
print(vecs)