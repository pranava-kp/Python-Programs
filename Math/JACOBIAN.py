from sympy import *
u,v,w=symbols('u v w')
x=u-(u*v)
y=(u*v)-(u*v*w)
z=(u*v*w)
dxu=diff(x,u)
dxv=diff(x,v)
dxw=diff(x,w)
dyu=diff(y,u)
dyv=diff(y,v)
dyw=diff(y,w)
dzu=diff(z,u)
dzv=diff(z,v)
dzw=diff(z,w)
J=det(Matrix([[dxu,dxv,dxw],[dyu,dyv,dyw],[dzu,dzv,dzw]]))
print('Jacobian J= ',J)