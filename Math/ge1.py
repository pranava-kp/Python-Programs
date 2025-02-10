from sympy import *
x,y=symbols('x y')
y=Function("y")(x)
y1=diff(y,x)
z1=dsolve(Eq(y1+y*tan(x),y**3*sec(x)),y)
print("General solutions of y=\n",z1)