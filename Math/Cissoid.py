import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-150,150,10000)
y=x*(np.sqrt(x/(4-x)))
z=-x*(np.sqrt((x)/(4-x)))
plt.plot(x,y,'r')
plt.plot(x,z,'b')
plt.title("Graph of Cissoid")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()