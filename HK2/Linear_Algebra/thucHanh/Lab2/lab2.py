import numpy as np
import math

def cau1():
    x = np.array([i for i in range(1, 6)])
    b = np.array([i for i in range(1, 7)])
    c = np.arange(1, 31)
    d = np.arange(1, 26)

    A = np.transpose(np.tile(x, (5, 1)))
    print("Matrix A:\n", A)

    B = np.tile(b, (5 ,1))
    print("Matrix B:\n", B)

    C = np.reshape(c, (6, 5)).T
    print("Matrix C:\n", C)

    D = np.reshape(c, (5, 6))
    print("Matrix D:\n", D)

def cau2():
    A = np.random.randint(1, 100, (5, 6))
    print("Matrix A:\n", A)

def cau3():
    A = np.reshape(np.arange(1, 10), (3, 3))
    A = np.flip(A, axis=1)
    print("Matrix A:\n", A)

def cau4():
    A = np.reshape(np.arange(1, 10), (3, 3))
    A = np.flip(A, axis=0)
    print("Matrix A:\n", A)

def cau5():
    Y = np.array([ [1, 2, 16, 31, 22], 
                   [2, 8, 12, 21, 23], 
                   [4, 9, 11, 14, 25],
                   [3, 6, 10, 16, 34] ])

    #a
    x = Y[1, 1:4]
    print("x: ", x)

    #b
    y = Y[0:5, 2:3]
    print("y: \n", y)

    #c
    A = Y[1:3, 1:5]
    print("A: \n", A)

    #d
    B = Y[0:5, 0:6:2]
    print("B: \n", B)

    #e
    C = Y[1:5, [0, 2, 3, 4]]
    print("C: \n", C)

    #f
    D = Y[Y > 12]
    print("D: \n", D)
    
def cau6():
    A = np.array([ [2, 4, 1],
                   [6, 7, 2],
                   [3, 5, 9] ])
    
    #a
    x1 = A[0]
    print("x1: \n", x1)

    #b
    Y = A[-2:]
    print("Y: \n", Y)

def cau7():
    A = np.array([ [2, 7, 9, 7],
                   [3, 1, 5, 6],
                   [8, 1, 2, 5] ])
    
    #a
    B = A[:, 1::2]
    print("B:\n", B)

    #b
    C = A[:, 0::2]
    print("C:\n", C)

    #c
    A = A.T
    print("A: \n", A)

def cau8():
    # 3 x 5
    T = np.array([ [12, 15, 10, 16, 12], 
                   [5, 9, 14, 7, 10],
                   [8, 12, 10, 9, 15] ])
    # 1 x 3
    A = np.array([2, 1, 3])

    totalSales = np.matmul(A, T)
    print(totalSales)
    
def cau10():
    A = np.array([ [-1, 4, 8],
                   [-9, 1, 2] ])

    B = np.array([ [5, 8],
                   [0, -6],
                   [5, 6] ])

    C = np.array([ [-4, 1],
                   [6, 5] ])

    D = np.array([ [-6, 3, 1],
                   [8, 9 , -2],
                   [6, -1, 5] ])
    
    #a
    cauA = np.matmul(A, B).T
    print("a/ (AB).T = \n", cauA)

    #b
    cauB = np.matmul(B, C).T
    print("b/ (BC).T = \n", cauB)

    #c
    cauC = C - C.T
    print("c/ C - C.T =\n", cauC)

    #d
    cauD = D - D.T
    print("d/ D - D.T =\n", cauD)

    #e
    E = (D.T).T
    print("e/ (D.T).T =\n", E)

    #f
    F = 2 * C.T
    print("f/ 2C.T =\n", F)

    #g
    G = A.T + B
    print("g/ A.T + b =\n", G)

    #h
    H = (A.T + B).T
    print("h/ (A.T + B).T =\n", H)

    #i
    I = (2*A.T  - 5*B).T
    print("i/ (2*A.T  - 5*B).T =\n", I)

    #j
    J = (-D).T
    print("j/ (-D).T =\n", J)

    #k
    K = -(D.T)
    print("k/ -(D.T) =\n", K)

    #l
    L = (C@C).T
    print("l/ (C^2).T = \n", L)

    #m
    M = (C.T)@(C.T)
    print("m/ (C.T)^2 = \n", M)

def cau11():
    A = np.array([ [2, 4, 1], 
                   [6, 7, 2],
                   [3, 5, 9] ])
    
    H = np.shape(A)
    
    #a
    print("a.")
    if (H[0] == H[1]):
        print("A is a square matrix")
    else:
        print("A is not a sqaure matrix")

    #So sanh hai ma tran
    def compareMatrix(A, B):
        if (np.shape(A) != np.shape(B)):
            return False
        
        for i in range(0, len(A[0])):
            for j in range(i , len(A[0])):
                if (A[i, j] != B[i, j]):
                    return False
        
        return True

    #b
    print("b.")
    if (compareMatrix(A, A.T)):
        print("Matrix A is symmetric")
    else:
        print("Matrx A is not symmetric")

    #c
    print("c.")
    if (compareMatrix(-A, A.T)):
        print("Matrix A is skew-symmetric")
    else:
        print("Matrix A is not skew-symmetric")
    
    #d
    print("d. Upper triangular matrix of A:")
    U = np.eye(3)
    for i in range(0, len(A[0])):
        for j in range(i, len(A[0])):
            U[i, j] = A[i, j]

    print(U)

    #e
    print("e. Lower triangular matrix of A:")
    L = np.eye(3)
    n = len(A[0])

    for i in range(n - 1, -1, -1):
        for j in range(i, -1, -1):
            L[i, j] = A[i, j]

    print(L)
            
def cau12():
    A = np.array([ [6, 0, 0, 5], 
                   [1, 7, 2, -5],
                   [2, 0, 0, 0],
                    [8, 3, 1, 8] ])

    B = np.array([ [1, -2, 5, 2],
                   [0, 0, 3, 0],
                   [2, -6, -7, 5],
                   [5, 0, 4, 4] ])

    C = np.array([ [3, 5, -8, 4],
                   [0, -2, 3, -7],
                   [0, 0, 1, 5],
                   [0, 0, 0, 2] ])

    D = np.array([ [4, 0, 0, 0],
                   [7, -1, 0, 0],
                   [2, 6, 3, 0],
                   [5, -8, 3, 0],
                   [5, -8, 4, -3]])

    E = np.array([ [4, 0, -7, 3, -5],
                   [0, 0, 2, 0, 0],
                   [7, 3, -6, 4, -8],
                   [5, 0, 5, 2, -3],
                   [0, 0, 9, -1, 2]])

    F = np.array([ [6, 3, 2, 4, 0],
                   [9, 0, -4, 1, 0],
                   [8, -5, 6, 7, 1],
                   [3, 0, 0, 0, 0],
                   [4, 2, 3, 2, 0]])
    
    print("Det(A) =", math.ceil(np.linalg.det(A)))
    print("Det(B) =", math.ceil(np.linalg.det(B)))
    print("Det(C) =", math.ceil(np.linalg.det(C)))
    # print("Det(D) =", math.ceil(np.linalg.det(D)))
    print("Det(E) =", math.ceil(np.linalg.det(E)))
    print("Det(F) =", math.ceil(np.linalg.det(F)))                
    
def cau15():
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


    A = np.array([ [2, 4, 5/2],
                [-3/4, 2, 1/4],
                [1/4, 1/2, 2] ])
    
    B = np.array([ [1, -1/2, 3/4],
                [ 3/2, 1/2, -2],
                [1/4, 1, 1/2]])
    
    print("A^(-1):\n", inverse(A))
    print("B^(-1):\n", inverse(B))





cau15()


