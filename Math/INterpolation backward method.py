from sympy import *
import numpy as np
n=6
x=np.zeros((n))
y=np.zeros((n,n))
x[0]=40
x[1]=50
x[2]=60
x[3]=70
x[4]=80
x[5]=90
y[0]=184
y[1]=204
y[2]=226
y[3]=250
y[4]=276
y[5]=304
for i in range(1,n):
    for j in range(n-1,i-2,-1):
        y[j][i]=y[j][i-1]-y[j-1][i-1]
print("\nIn backward difference table \n")
for i in range(0,n):
    print("%0.2f"%(x[i]),end="")
    for j in range(0,i+1):
        print("\t\t%.2f"%(y[i][j]),end="")
    print("\n")
f=[]
t=symbols('t')
p=(t-x[n-1])/(x[1]-x[0])
f.append(p)
for i in range(1,n-1):
    f.append(f[i-1]*(p+i)/(i+1))###############
    poly=y[n-1][0]
for i in range(n-1):
    poly=poly+y[n-1][i+1]*f[i]
simp_poly=simplify(poly)
print("\nThe interpolating polynomial is \n")
print(simp_poly)
a=85
interpol=lambdify(t,simp_poly)
result=interpol(a)
print("\nThe value of function at ",a," is \n",result)