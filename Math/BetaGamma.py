from sympy import *
m=float(input("m:"))
n=float(input("n:"))
s=beta(m,n)
t=gamma(n)
print("Beta ('m,n')is %3.3f"%s)
print("Gamma ('n')is %3.3f"%t)