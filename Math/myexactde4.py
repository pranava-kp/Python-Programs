from sympy import *
x,y=symbols('x y')
M=x*y**3+y
N=2*(x**2*y**2+x+y**4)
dmy=diff(M,y)
dnx=diff(N,x)
inf=1
if(dmy-dnx!=0):
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