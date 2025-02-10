from sympy import *
A=Matrix([[1,2,3],[3,4,4],[7,10,12]])
B=Matrix([[0],[0],[0]])
r=A.rank()
n=A.shape[1]
if(r==n):
    print("System has trivial solution")
else:
    print("System has ",(n-r)," non trivial solutions")