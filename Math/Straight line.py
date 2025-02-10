import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,1000)
y=(3*x)+4
z=(-5*x)+1
m=(2*x)-3
plt.plot(x,y,'r.')
plt.plot(x,z,'b.')
plt.plot(x,m,'g.')
plt.title("Graph of straight line")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()