from sympy import *
A=Matrix([[1,3,-2],[2,-1,4],[1,-11,14]])
B=Matrix([[0],[0],[0]])
r=A.rank()
n=A.shape[1]
if(r==n):
    print("System has trivial solution")
else:
    print("System has ",(n-r)," non trivial solutions")