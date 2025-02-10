from sympy import *
from sympy.vector import *
N=CoordSys3D("N")
x,y,z=symbols("x y z")
F=(N.x**2*N.y*N.z)*N.i+(N.x*N.y**2*N.z)*N.j+(N.x*N.y*N.z**2)*N.k
delop=Del()
curlA=delop.cross(F)
print(curlA)
print(curl(F))