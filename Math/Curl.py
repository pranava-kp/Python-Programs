from sympy.vector import *
from sympy import *
N=CoordSys3D('N')
x,y,z=symbols('x y z')
A=N.x*N.y**2*N.i+2*N.x*N.y*N.z*N.j-3*N.y*N.z**2*N.k
delop=Del()
curlA=delop.cross(A)
print(f"\nCurl of {A} is \n",curl(A))