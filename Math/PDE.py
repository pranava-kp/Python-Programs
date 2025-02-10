from sympy import *
x,y=symbols('x y')
u=atan(y/x)
dux=diff(u,x)
duy=diff(u,y)
duxy=diff(dux,y)
duyx=diff(duy,x)
if duxy == duyx :
    print("Mixed partial derivations are equal")
else :
    print("Mixed partial derivations are unequal")

uxx=diff(dux,x)
uyy=diff(duy,y)
w=uxx+uyy
w1=simplify(w)
print("Answer is ",float(w1))
