from sympy import *
x,y=symbols('x y')
I1=integrate(x**2+y**2,y,x)
I2=integrate(x**2+y**2,x,y)
print(I1)
print(I2)
if I1 == I2:
    print("Integrals are equal")
else:
    print("Integrals are not equal")