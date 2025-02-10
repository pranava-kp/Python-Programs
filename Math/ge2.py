from sympy import *
x,y=symbols('x y')
y=Function("y")(x)
y1=diff(y,x)
z1=dsolve(Eq(x**3*y1-x**2*y,-y**4*cos(x)),y)
print("General solutions of y=\n",z1)