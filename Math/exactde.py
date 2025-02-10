from sympy import *
x,y=symbols('x y')
M=x*y**3+y
N=2*(x**2*y**2+x+y**4)
dmy=diff(M,y)
dnx=diff(N,x)
if(dmy==dnx):
    print("Equation is exact")
    I1=integrate(M,x).doit()
    I2=(integrate(N,y).doit()).subs(x,0)
    W=I1+I2
    print("Solution: ",W," + C")
else:
    print("Equation is not exact")
    d=simplify(dmy-dnx)
    f=simplify(d/N)
    g=simplify(d/M)
if(diff(f,y)==0):
    inf=exp(integrate(f,x))
else:
    inf=exp(-(integrate(g,y)))
print("Integrating factor is ",inf)
M1=M*inf
N1=N*inf
I1=integrate(M1,x).doit()
I2=(integrate(N1,y).doit()).subs(x,0)
W=I1+I2
print("Solution: ",W," = C")