from sympy import plot_implicit, symbols, Eq
x, y = symbols('x y')
a=2
p1=plot_implicit(Eq(x**3+y**3,3*a*x*y),(x,-5,5),(y,-5,5),
title="Folio of de-cartes")
pli=plot_implicit(p1)
