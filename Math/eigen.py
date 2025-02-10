import numpy as np
from sympy import *
X=np.array(([1,0,0]))
A=np.array(([2,0,1],[0,2,0],[1,0,2]))
for i in range(20):
    X=np.dot(A,X)
    lambda_1=(abs(X)).max()
    X=X/X.max()
print("Eigen value : %0.4f"%lambda_1)
print("Eigen vector : ")
pprint(X)