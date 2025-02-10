from sympy import *
x,y=symbols('x y')
M=1+exp(x/y)
N=exp(x/y)*(1-x/y)
dmy=diff(M,y)
dnx=diff(N,x)
inf=1
if(dmy!=dnx):
    print("Equation is not exact")
    d=simplify(dmy-dnx)
    f=simplify(d/N)
    g=simplify(d/M)
    if(diff(f,y)==0):
        inf=simplify(exp(integrate(f,x)))
    else:
        inf=simplify(exp(-(integrate(g,y))))
    M*=inf
    N*=inf
else:
    print("Equation is exact")
print("Integrating factor is ",inf)
I1=integrate(M,x).doit()
I2=(integrate(N,y).doit()).subs(x,0)
W=I1+I2
print("Solution: ",W," = C")