import numpy as np

A = np.array([ [2, 4, 5/2],
               [-3/4, 2, 1/4],
               [1/4, 1/2, 2] ])

B = np.array([ [1, -1/2, 3/4],
                [ 3/2, 1/2, -2],
                [1/4, 1, 1/2]])

def det(A):
    return A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]

def inverse(A):
    n = len(A[0])
    B = []


    for i in range(0, n):
        for j in range(0, n):
            T = []
            for k in range(0, n):
                for t in range(0, n):
                    if (i != k and j != t):
                        T.append(A[k, t])
            
            B.append(det(np.reshape(T, (2, 2))))
        
    return ((1/np.linalg.det(A)) * np.reshape(B, (3, 3)).T)

print(inverse(A))
    
