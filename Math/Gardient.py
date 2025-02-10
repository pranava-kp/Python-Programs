from sympy.vector import *
from sympy import *
N = CoordSys3D('N')
x, y, z = symbols('x y z')
A = N.x**2*N.y*N.z
delop = Del()
print(delop(A))
gradA = gradient(A)
print(f"\nGradient of {A} is:\n", gradA)