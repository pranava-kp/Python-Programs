from sympy import *
x,y,z=symbols('x y z')
I=integrate(x*y**2*z,(z,1,2),(y,1,3),(x,0,2))
print(I)