from sympy import *
import numpy as np
n=5
x=np.zeros((n))
y=np.zeros((n,n))
x[0]=1
x[1]=2
x[2]=3
x[3]=4
x[4]=5
y[0]=10
y[1]=26
y[2]=58
y[3]=112
y[4]=194
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]
print("\nIn forward difference table \n")
for i in range(0,n):
    print("%0.2f"%(x[i]),end="")
    for j in range(0,n-i):
        print("\t\t%.2f"%(y[i][j]),end="")
    print("\n")
t=symbols('t')
f=[]
p=(t-x[0]/(x[1]-x[0]))
f.append(p)
for i in range(1,n-1):
    f.append(f[i-1]*(p-i)/(i+1))
    poly=y[0][0]
for i in range(n-1):
    poly=poly+y[0][i+1]*f[i]
simp_poly=simplify(poly)
print("\nThe interpolating polynomial is \n")
print(simp_poly)
a=1.4
interpol=lambdify(t,simp_poly)
result=interpol(a)
print("\nThe value of function at ",a," is \n",result)