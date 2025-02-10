import numpy as np
from sympy import *
A=np.array([[1,1,3],[1,5,1],[3,1,1]])
X=np.array([1,1,1])
for i in range(20):
    X=np.dot(A,X)
    lambda1=abs(X.max())
    X=X/X.max()
print("Eighen value %0.4f"%lambda1)
print("Eigen vector ",X)