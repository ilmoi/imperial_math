import numpy as np
from scipy import spatial



def pairwise_distance_matrix(X, Y):
    """Compute the pairwise distance between rows of X and rows of Y

    Arguments
    ----------
    X: ndarray of size (N, D)
    Y: ndarray of size (M, D)
    
    Returns
    --------
    distance_matrix: matrix of shape (N, M), each entry distance_matrix[i,j] is the distance between
    ith row of X and the jth row of Y (we use the dot product to compute the distance).
    """
    N, D = X.shape
    M, _ = Y.shape
    distance_matrix = np.zeros([N,M])
    for i,n in enumerate(X):
        for j,m in enumerate(Y):
            distance_matrix[i][j] = np.sqrt(np.dot(n-m,n-m))
    return distance_matrix

X = np.array([[1,2,3],[2,3,4],[3,4,5]])
Y = np.array([[1,2,3],[2,3,4]])
z = pairwise_distance_matrix(X,Y)
#z2 = spatial.distance.pdist(X,metric='euclidean')
#z2 = spatial.distance.squareform(z2)

z3 = spatial.distance.cdist(X,Y)
z3 = spatial.distance.squareform(z3)

print(z)
print(z2)