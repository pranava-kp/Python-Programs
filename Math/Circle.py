from sympy import plot_implicit, symbols, Eq
x, y = symbols('x y')
r=5
p1=plot_implicit(Eq((x**2)+(y**2),r**2),(x,-6,6),(y,-6,6),
    title="Circle")
pli=plot_implicit(p1) 
