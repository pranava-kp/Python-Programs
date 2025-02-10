from sympy.vector import *
from sympy import *
N=CoordSys3D('N')
x,y,z=symbols('x y z')
A=((N.x**2*N.y)*N.i)+((N.z**2*N.y)*N.j)+((N.x**2*N.z)*N.k)
delop=Del()
divA=delop.dot(A)
print(divA)
print(f"\n Derivative of {A} is \n",divergence(A))