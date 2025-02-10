from sympy import *
x,y,z=symbols('x y z')
A=Matrix([[1,-4,7],[3,8,-2],[7,-8,26]])
B=Matrix([[14],[13],[5]])
AB=A.col_insert(A.shape[1],B)
rA=A.rank()
rAB=AB.rank()
n=A.shape[1]
print("The co-efficient matrix is ")
pprint(A)
print("\nThe rank of co-efficient matrix is ",rA)
print("\nThe augumented matrix is ")
pprint(AB)
print("\nThe rank of augumented matrix is ",rAB)
print("The number of unknowns are ",n)
if(rA==rAB):
    if(rA==n):
        print("\nThe system has unique solution")
    else:
        print("\nThe system has infinite solutions")
    print(solve_linear_system(AB,x,y,z))    
else:
    print("The system of equations is inconsistent")