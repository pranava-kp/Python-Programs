import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,4,1000)
y=x*(np.sqrt((5+x)/(5-x)))
z=-x*(np.sqrt((5+x)/(5-x)))
plt.plot(x,y,'r')
plt.plot(x,z,'b')
plt.title("Graph of Stophoid")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()